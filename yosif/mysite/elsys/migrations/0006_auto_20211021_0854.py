# Generated by Django 3.2.8 on 2021-10-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0005_auto_20211021_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='description',
            new_name='info',
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='made',
            field=models.DateTimeField(),
        ),
    ]
