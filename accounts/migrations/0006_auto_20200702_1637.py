# Generated by Django 3.0.7 on 2020-07-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200702_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'مرد'), (2, 'زن'), (3, 'حقوقی')], null=True, verbose_name='جنسیت'),
        ),
    ]
