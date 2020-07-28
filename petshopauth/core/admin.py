from django.contrib import admin
from petshopauth.core import models

# Register your models here.

class PetAdmin(admin.ModelAdmin):
  list_display = ('nome', 'raca', 'idade')
  search_fields = ['nome', 'raca', 'idade']

admin.site.register(models.Pet)