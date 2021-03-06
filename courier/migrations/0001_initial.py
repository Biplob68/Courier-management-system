# Generated by Django 2.1.5 on 2020-01-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_Description', models.CharField(max_length=300)),
                ('product_type', models.CharField(max_length=100)),
                ('product_image', models.ImageField(default='', upload_to='courier/images')),
                ('product_weight', models.FloatField()),
                ('product_price', models.FloatField()),
            ],
        ),
    ]
