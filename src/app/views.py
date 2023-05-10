from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from app.models import User, Comment, Order
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app.forms import RegisterForm, CommentForm, OrderForm



# Create your views here.
def index_page(request):
    return render(request, 'index.html', context={'page': 'index'})

def catalog(request):
    if request.method == 'POST':
        today = date.today()
        form = Order(name=request.POST['fullname'], phone=request.POST['phone'], email=request.POST['email'], address=request.POST['address'], date = today.strftime('%d.%m.%Y'))
        form.save()
        messages.success(request, 'Ваш заказ отправлен успешно!')
        return redirect('catalog')
    else:
        form = OrderForm()
    return render(request, 'catalog.html', context={'page': 'catalog',})

def about(request):
    if request.method == 'POST':
        today = date.today()
        form = Comment(name=request.POST['username'], message=request.POST['message'], date=today.strftime('%d.%m.%Y'))
        form.save()
        return  redirect('about')
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'about.html', context={'page': 'about', 'comments': comments})



class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)

        user.save()
        return user



