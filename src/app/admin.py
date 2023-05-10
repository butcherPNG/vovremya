from django.contrib import admin
from app.models import Comment, User, Order

# Register your models here.
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Order)