# Generated by Django 4.2.1 on 2023-06-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0003_rename_house_contact_house_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(verbose_name='Дата выхода'),
        ),
    ]