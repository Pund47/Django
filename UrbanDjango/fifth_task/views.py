from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm

info = {}
user_list = ["Злодей", "Маруся"]
def sign_up_by_django(request):
    pass
'''
def sign_up_by_django(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if not (password != repeat_password) and (username in user_list):
            user_list.append(username)
#            print(f"username: {username}")
#            print(f"password: {password}")
#            print(f"repeat_password: {repeat_password}")
#            print(f"age: {age}")
            return HttpResponse(f"Приветствуем, {username}!")

        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
#            print(info)
            return HttpResponse(f"Пароли не совпадают!")

        if username in user_list:
            HttpResponse(f"Пользователь уже существует!")


    return render(request,'registration_page.html')
'''


def sign_up_by_html(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Обработка данных формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
    else:
        form = ContactForm()
    return render(request,'registration_page.html',{'form': form})
