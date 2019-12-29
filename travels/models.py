from django.db import models
from django_countries.fields import CountryField
from users import models as user_models
from cores import models as core_models


# Create your models here.


class Travel(core_models.TimeStampedModel):
    """ Travel Model Definition """

    name = models.CharField(max_length=30)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    start = models.DateField()
    end = models.DateField()
    companion = models.ForeignKey(user_models.User, on_delete=models.CASCADE)


def __str__(self):
    return self.name
