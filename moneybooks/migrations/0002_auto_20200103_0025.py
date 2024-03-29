# Generated by Django 2.2.5 on 2020-01-02 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travels', '0001_initial'),
        ('moneybooks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='moneybook',
            name='companions',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moneybook',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='travels.Travel'),
        ),
        migrations.AddField(
            model_name='moneybook',
            name='paidperson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paidperson', to=settings.AUTH_USER_MODEL),
        ),
    ]
