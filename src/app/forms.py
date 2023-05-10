
from django import forms
from app.models import Comment
from app.models import User, Order
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'date')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'address', 'date')


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин', required=True, max_length=254)
    email = forms.EmailField(label='Почта', required=True, max_length=254)
    password1 = forms.CharField(label='Пароль', required=True, max_length=254, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', required=True, max_length=254, widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
            return user


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



