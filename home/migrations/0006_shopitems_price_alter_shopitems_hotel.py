# Generated by Django 5.2.4 on 2025-07-15 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_shopitems_type_alter_shopitems_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitems',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='shopitems',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shop_items', to='home.hotels'),
        ),
    ]
