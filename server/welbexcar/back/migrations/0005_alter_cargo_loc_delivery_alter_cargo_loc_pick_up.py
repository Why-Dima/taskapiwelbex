# Generated by Django 4.2.1 on 2023-05-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0004_car_zip_cargo_zip_alter_location_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='loc_delivery',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='loc_pick_up',
            field=models.PositiveIntegerField(),
        ),
    ]