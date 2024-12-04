from django import forms

from .models import Cliente
class ClientForm(forms.ModelForm):
    # nome = forms.CharField(label="Nome do cliente", max_length=100)
    # idade = forms.IntegerField(label="Idade do cliente")
    # data_nascimento = forms.DateField(label="Data de nascimento")
    # is_ativo = forms.BooleanField(label="Se o cliente está ativo")
    class Meta:
        model = Cliente
        fields='__all__'