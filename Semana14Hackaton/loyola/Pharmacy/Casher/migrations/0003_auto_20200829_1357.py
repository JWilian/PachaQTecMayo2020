# Generated by Django 3.1 on 2020-08-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Casher', '0002_auto_20200829_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='forbaby',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='syrup',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='tablet',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='toiletries',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='vitamins',
            field=models.BooleanField(default=True),
        ),
    ]
