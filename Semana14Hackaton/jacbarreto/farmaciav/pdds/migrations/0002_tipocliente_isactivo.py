# Generated by Django 3.1 on 2020-09-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipocliente',
            name='isActivo',
            field=models.CharField(choices=[('AC', 'Activo'), ('IA', 'Inactivo')], default='AC', max_length=2),
        ),
    ]
