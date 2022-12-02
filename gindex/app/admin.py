from django.contrib import admin

# Register your models here.
from . import  models


admin.site.register(models.Term)
admin.site.register(models.Keyword)