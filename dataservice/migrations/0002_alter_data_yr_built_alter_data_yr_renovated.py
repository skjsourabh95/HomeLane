# Generated by Django 4.0.4 on 2022-04-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='yr_built',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='yr_renovated',
            field=models.IntegerField(),
        ),
    ]
