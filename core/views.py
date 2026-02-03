from django.shortcuts import render
from django.db.models import Count, Sum, Q  # <--- Adicionamos o Q aqui
from django.contrib.auth.decorators import login_required
from .models import Cliente, Contrato, ChamadoTecnico

@login_required
def dashboard(request):
    # --- LÓGICA DE BUSCA (NOVO) ---
    query = request.GET.get('q') # Pega o que foi digitado na barra de busca
    resultados_busca = None
    
    if query:
        # Busca por Nome OU CPF (icontains = ignora maiúscula/minúscula)
        resultados_busca = Cliente.objects.filter(
            Q(nome_completo__icontains=query) | 
            Q(cpf_cnpj__icontains=query)
        )
    # ------------------------------

    # Totais Gerais
    total_clientes = Cliente.objects.count()
    contratos_ativos = Contrato.objects.filter(status='ATIVO').count()
    
    faturamento_mensal = Contrato.objects.filter(status='ATIVO').aggregate(
        total=Sum('plano__valor_mensal')
    )['total'] or 0

    chamados_pendentes = ChamadoTecnico.objects.exclude(status='CONCLUIDO').count()

    # Dados para o Gráfico
    dados_grafico = ChamadoTecnico.objects.values('tipo').annotate(total=Count('id'))
    labels_grafico = [item['tipo'] for item in dados_grafico]
    valores_grafico = [item['total'] for item in dados_grafico]

    context = {
        'total_clientes': total_clientes,
        'contratos_ativos': contratos_ativos,
        'faturamento_mensal': faturamento_mensal,
        'chamados_pendentes': chamados_pendentes,
        'labels_grafico': labels_grafico,
        'valores_grafico': valores_grafico,
        'usuario': request.user,
        
        # Enviando os dados da busca para o HTML
        'query': query,
        'resultados_busca': resultados_busca,
    }

    return render(request, 'core/dashboard.html', context)