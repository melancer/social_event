# Generated by Django 3.0.7 on 2020-07-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200705_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=11, null=True, verbose_name='تلفن همراه'),
        ),
    ]