# Generated by Django 2.1.5 on 2020-01-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0014_auto_20200123_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(default='', max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('gender', models.CharField(max_length=20)),
                ('user_type', models.CharField(max_length=20)),
            ],
        ),
    ]
