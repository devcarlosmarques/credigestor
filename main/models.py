from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.IntegerField()
    proposta = models.CharField(max_length=255)
    banco = models.CharField(max_length=255)
    prazo = models.IntegerField()
    valor = models.FloatField()
    parcela = models.FloatField()
    STATUS_CHOICES = [
        ("AND", "ANDAMENTO"),
        ("REP", "REPROVADO"),
        ("INT", "INTEGRADO"),
        ("PEN", "PENDENTE"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, blank=False, null=False)

    def __str__(self):
        return self.nome
    
class Proposta(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    proposta = models.CharField(max_length=255)

    ORGAO_CHOICES = [
        ("INSS", "INSS"),
        ("FEDERAL", "FEDERAL"),
        ("PREFEITURA DO RECIFE", "PREFEITURA DO RECIFE"),
        ("GOVERNO DE PERNAMBUCO", "GOVERNO DE PERNAMBUCO"),
        ("EXERCITO", "EXERCITO"),
        ("AERONAUTICA", "AERONAUTICA"),
        ("MARINHA", "MARINHA"),
    ]
    orgao = models.CharField(choices=ORGAO_CHOICES, blank=False, null=False, max_length=60)

    OPERACAO_CHOICES = [
        ("NOVO", "NOVO"),
        ("REFIN", "REFIN"),
        ("PORTABILIDADE", "PORTABILIDADE"),
        ("CARTAO CONSIGNADO", "CARTAO CONSIGNADO"),
        ("CARTAO BENEFICIO", "CARTAO BENEFICIO"),
    ]
    operacao = models.CharField(choices=OPERACAO_CHOICES, blank=False, null=False, max_length=60)

    BANCO_CHOICES = [
        ("BMG", "BMG"),
        ("ITAU", "ITAU"),
        ("DAYCOVAL", "DAYCOVAL"),
        ("C6 BANK", "C6 BANK"),
        ("BANRISUL", "BANRISUL"),
        ("MERCANTIL", "MERCANTIL"),
        ("OLE CONSIGNADO", "OLE CONSIGNADO"),
        ("BRADESCO", "BRADESCO"),
        ("SAFRA", "SAFRA"),
    ]
    banco = models.CharField(choices=BANCO_CHOICES, blank=False, null=False, max_length=60)

    valor = models.FloatField()
    parcela = models.FloatField()
    prazo = models.IntegerField()
    STATUS_CHOICES = [
        ("AND", "ANDAMENTO"),
        ("REP", "REPROVADO"),
        ("INT", "INTEGRADO"),
        ("PEN", "PENDENTE"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, blank=False, null=False)

    def __str__(self):
        return self.nome
    
class Noticia(models.Model):
    noticia = models.CharField(max_length=50)
    descricao = models.TextField()
    data = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.noticia
