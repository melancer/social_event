# Generated by Django 3.0.7 on 2020-07-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organ_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='عنوان سازمان'),
        ),
    ]
