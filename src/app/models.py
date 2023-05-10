from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя пользователя')
    message = models.TextField(max_length=2000, blank=False, verbose_name='Комментарий')
    date = models.CharField(max_length=20, blank=False, verbose_name='Время')

    def __str__(self):
        return 'Комментарий от ' + self.name

class Order(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=20, blank=False, verbose_name='Номер телефона')
    address = models.CharField(max_length=500, blank=False, verbose_name='Адрес')
    email = models.CharField(max_length=100, blank=False, verbose_name='Почта')
    date = models.CharField(max_length=20, blank=False, verbose_name='Время')

    def __str__(self):
        return 'Заказ от ' + self.name


class User(AbstractUser):
    username = models.CharField(max_length=20, blank=False, verbose_name='Имя пользователя', unique=True)
    email = models.CharField(max_length=100, blank=False, verbose_name='Почта', unique=True)
    password = models.CharField(max_length=52, blank=False, verbose_name='Пароль')


    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

