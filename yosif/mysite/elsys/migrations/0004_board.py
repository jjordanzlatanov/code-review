# Generated by Django 3.2.8 on 2021-10-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0003_alter_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=50)),
                ('trainNumber', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
