from django import forms
from .models import Proposta

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'