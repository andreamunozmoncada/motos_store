# Generated by Django 5.0.6 on 2024-06-22 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('state', models.CharField(max_length=255)),
                ('displacement', models.IntegerField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='moto_marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motos_store.marca')),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motos_store.moto')),
            ],
        ),
    ]