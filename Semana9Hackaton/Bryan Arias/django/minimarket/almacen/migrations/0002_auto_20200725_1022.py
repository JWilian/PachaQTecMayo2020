# Generated by Django 3.0.8 on 2020-07-25 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]
