# Generated by Django 3.0.7 on 2020-06-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventing', '0002_event_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(default='mehdi', upload_to=''),
            preserve_default=False,
        ),
    ]