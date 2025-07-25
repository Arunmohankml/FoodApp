# Generated by Django 5.2.4 on 2025-07-14 02:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_hotels_sections_items_shopitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='managers',
            field=models.ManyToManyField(blank=True, related_name='managed_hotels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hotels',
            name='owner',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('hotel', 'Hotel owner'), ('manager', 'Hotel manager'), ('user', 'Normal user')], default='user', max_length=15),
        ),
    ]
