# Generated by Django 5.0.6 on 2024-06-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='moto',
            name='displacement',
            field=models.IntegerField(),
        ),
    ]