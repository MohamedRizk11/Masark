# Generated by Django 5.0.4 on 2024-04-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masark', '0002_alter_station_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='ID',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='ID',
            field=models.IntegerField(verbose_name='ID'),
        ),
    ]
