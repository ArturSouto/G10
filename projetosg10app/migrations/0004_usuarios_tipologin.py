# Generated by Django 4.2.6 on 2023-10-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardimdogotasapp', '0003_usuarios_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='tipologin',
            field=models.IntegerField(choices=[(1, 'Administrador'), (2, 'Padrinho'), (3, 'Voluntário')], default=1),
        ),
    ]
