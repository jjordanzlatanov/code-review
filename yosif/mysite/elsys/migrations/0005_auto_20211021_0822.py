# Generated by Django 3.2.8 on 2021-10-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0004_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='carrier',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='board',
            name='trainNumber',
            field=models.CharField(max_length=100),
        ),
    ]
