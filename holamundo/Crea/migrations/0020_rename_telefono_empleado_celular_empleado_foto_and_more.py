# Generated by Django 5.0.2 on 2024-02-24 05:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crea', '0019_alter_propiedad_disponible_foto_propiedad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='telefono',
            new_name='celular',
        ),
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.FileField(blank=True, upload_to='foto_empleado/'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Perfil_Usuario',
        ),
    ]