# Generated by Django 5.0.2 on 2024-02-09 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad_posible',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pk', to='Crea.p_cliente'),
        ),
    ]