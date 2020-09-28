# Generated by Django 2.1.5 on 2020-01-22 17:39

import courier.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0009_auto_20200122_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[(courier.models.OrderStatus(('Placed Order',)), 'Placed'), (courier.models.OrderStatus(('Confirmed Order',)), 'Confirmed'), (courier.models.OrderStatus(('Confirmed Order',)), 'Confirmed'), (courier.models.OrderStatus(('Dispatched Product',)), 'Dispatched'), (courier.models.OrderStatus(('Reached Product',)), 'Reached'), (courier.models.OrderStatus('Delivered Product'), 'Delivered')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='expectedDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
