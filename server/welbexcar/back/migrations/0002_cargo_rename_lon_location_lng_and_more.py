# Generated by Django 4.2.1 on 2023-05-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_pick_up', models.FloatField()),
                ('loc_delivery', models.FloatField()),
                ('weight', models.PositiveSmallIntegerField(max_length=4)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.RenameField(
            model_name='location',
            old_name='lon',
            new_name='lng',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='state',
            new_name='state_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='index',
            new_name='zip',
        ),
        migrations.AddField(
            model_name='car',
            name='carrying_capacity',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]
