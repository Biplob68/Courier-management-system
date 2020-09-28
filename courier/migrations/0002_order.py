# Generated by Django 2.1.5 on 2020-01-21 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_name', models.CharField(max_length=90)),
                ('sender_email', models.CharField(max_length=111)),
                ('sender_address', models.CharField(max_length=111)),
                ('sender_phone', models.CharField(default='', max_length=111)),
                ('receiver_name', models.CharField(max_length=90)),
                ('receiver_email', models.CharField(max_length=111)),
                ('receiver_address', models.CharField(max_length=111)),
                ('receiver_phone', models.CharField(default='', max_length=111)),
                ('product_name', models.CharField(max_length=111)),
                ('weight', models.FloatField()),
                ('quantity', models.FloatField()),
                ('dateTime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
