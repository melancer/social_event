# Generated by Django 3.0.7 on 2020-06-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('subject', models.CharField(choices=[('computer science', 'علوم رایانه'), ('data science', 'علم داده'), ('big data', 'کلان داده'), ('artificial intelligence', 'هوش مصنوعی'), ('security', 'امنیت'), ('software engineering', 'مهندسی نرافزار'), ('develop', 'توسعه'), ('cryptography', 'رمزنگاری'), ('crypto currency', 'رمز ارز'), ('IOT', 'اینترنت اشیا'), ('startup', 'استارتاپ')], max_length=30, verbose_name='موضوع')),
                ('organizer', models.CharField(max_length=50, verbose_name='برگزار کننده')),
                ('start_date', models.DateTimeField(verbose_name='زمان شروع')),
                ('end_date', models.DateTimeField(verbose_name='زمان پایان')),
                ('details', models.TextField(max_length=2000, verbose_name='درمورد رویداد')),
                ('ticket', models.BooleanField()),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویداد',
            },
        ),
    ]
