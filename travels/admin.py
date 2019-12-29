from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Travel)
class TravelAdmin(admin.ModelAdmin):
    pass
