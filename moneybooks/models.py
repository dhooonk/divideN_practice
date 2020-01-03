from django.db import models
from cores import models as core_models

# Create your models here.


class Moneybook(core_models.TimeStampedModel):

    """ Moneybook Model Definition """
    CURRENCY_AMERICA = "en"
    CURRENCY_KOREAN = "kr"
    CURRENCY_EUROPE = "eu"
    CURRENCY_CHOICES = ((CURRENCY_AMERICA, "USD"),
                        (CURRENCY_KOREAN, "KRW"), (CURRENCY_EUROPE, "EUR"))

    CATEGORY_EAT = "ea"
    CATEGORY_TICKET = "ti"
    CATEGORY_CHOICES = ((CATEGORY_EAT, "EAT"), (CATEGORY_TICKET, "TICKET"))

    paidperson = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="paidperson")
    companions = models.ManyToManyField(
        "users.User", blank=True)
    price = models.IntegerField(default=0)
    location = models.ForeignKey(
        "travels.Travel", on_delete=models.CASCADE, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=2, default=CURRENCY_KOREAN)
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=2, blank=True)
    memo = models.TextField(blank=True)
