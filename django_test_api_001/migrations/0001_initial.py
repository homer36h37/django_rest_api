# Generated by Django 5.0.2 on 2024-02-26 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('birthdate', models.DateTimeField(verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('birthdate', models.DateTimeField(verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('quantity', models.IntegerField(verbose_name='В наличии')),
                ('price', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('сlient', models.CharField(max_length=300, verbose_name='Клиент')),
                ('employee', models.CharField(max_length=300, verbose_name='Сотрудник')),
                ('created_date', models.DateTimeField()),
                ('product', models.ManyToManyField(to='django_test_api_001.product', verbose_name='Товары')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_employee', models.CharField(max_length=300, verbose_name='ФИО')),
                ('full_name_client', models.CharField(max_length=300, verbose_name='ФИО')),
                ('quantity_clients', models.IntegerField(verbose_name='Количество клиентов')),
                ('quantity_products', models.IntegerField(verbose_name='Количество товаров')),
                ('total_price', models.IntegerField(verbose_name='Сумма продаж')),
                ('created_date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_test_api_001.client', verbose_name='id клиента')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_test_api_001.employee', verbose_name='id сотрудника')),
            ],
        ),
    ]
