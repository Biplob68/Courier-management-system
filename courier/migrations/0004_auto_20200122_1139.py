# Generated by Django 2.1.5 on 2020-01-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0003_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
