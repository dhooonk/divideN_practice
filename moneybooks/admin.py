from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Moneybook)
class MoneybookAdmin(admin.ModelAdmin):

    list_display = ("paidperson",
                    "price",
                    "location",
                    "currency",
                    "category"
                    )
    pass
