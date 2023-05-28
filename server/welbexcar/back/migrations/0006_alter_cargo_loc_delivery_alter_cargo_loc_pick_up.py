# Generated by Django 4.2.1 on 2023-05-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_alter_cargo_loc_delivery_alter_cargo_loc_pick_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='loc_delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc_delivery', to='back.location'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='loc_pick_up',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loc_pick_up', to='back.location'),
        ),
    ]
