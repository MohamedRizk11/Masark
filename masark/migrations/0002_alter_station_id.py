# Generated by Django 5.0.4 on 2024-04-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='ID',
            field=models.IntegerField(max_length=35, verbose_name='ID'),
        ),
    ]