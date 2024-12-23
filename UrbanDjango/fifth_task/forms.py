from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30,label="Введите логин")
    password = forms.CharField(label="Введите пароль")
    repeat_password = forms.CharField(label="Повторите пароль")
    age = forms.CharField(widget=forms.NumberInput , label="Введите свой возраст")