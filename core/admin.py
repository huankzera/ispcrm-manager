from django.contrib import admin
from .models import Cliente, PlanoInternet, Contrato, ChamadoTecnico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'telefone', 'endereco_instalacao')
    search_fields = ('nome_completo', 'cpf_cnpj')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'plano', 'status', 'ip_fixo')
    list_filter = ('status', 'plano')
    search_fields = ('cliente__nome_completo',)

@admin.register(ChamadoTecnico)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'tipo', 'prioridade', 'status', 'data_abertura')
    list_filter = ('status', 'tipo', 'prioridade')
    actions = ['marcar_concluido']

    def marcar_concluido(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='CONCLUIDO', data_fechamento=timezone.now())
    marcar_concluido.short_description = "Marcar chamados selecionados como Concluídos"

admin.site.register(PlanoInternet)