from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua mensagem...'}))
