from django.db import models
from django.utils import timezone

# Opções de Status para reutilização
STATUS_CONTRATO = [
    ('ATIVO', 'Ativo'),
    ('SUSPENSO', 'Suspenso (Financeiro)'),
    ('CANCELADO', 'Cancelado'),
]

STATUS_CHAMADO = [
    ('ABERTO', 'Aberto'),
    ('EM_ANDAMENTO', 'Em Atendimento'),
    ('CONCLUIDO', 'Concluído'),
]

class PlanoInternet(models.Model):
    nome = models.CharField(max_length=100, help_text="Ex: Fibra 500MB")
    velocidade_download = models.IntegerField(help_text="Em Mbps")
    velocidade_upload = models.IntegerField(help_text="Em Mbps")
    valor_mensal = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.valor_mensal}"

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco_instalacao = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    plano = models.ForeignKey(PlanoInternet, on_delete=models.PROTECT)
    data_inicio = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CONTRATO, default='ATIVO')
    ip_fixo = models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', help_text="Opcional: IP Fixo do cliente")
    mac_address = models.CharField(max_length=17, blank=True, null=True, help_text="MAC da ONU/Roteador")

    def __str__(self):
        return f"Contrato #{self.id} - {self.cliente.nome_completo}"

class ChamadoTecnico(models.Model):
    TIPO_PROBLEMA = [
        ('SEM_CONEXAO', 'Sem Conexão'),
        ('LENTIDAO', 'Lentidão'),
        ('FINANCEIRO', 'Dúvida Financeira'),
        ('MUDANCA_ENDERECO', 'Mudança de Endereço'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_PROBLEMA)
    prioridade = models.IntegerField(default=1, choices=[(1, 'Baixa'), (2, 'Média'), (3, 'Alta')])
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHAMADO, default='ABERTO')
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Chamado {self.id} - {self.get_tipo_display()}"