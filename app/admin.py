from django.contrib import admin
from django.contrib.admin.decorators import register
from app.models import TODO
# Register your models here.
admin.site.register(TODO)