# Generated by Django 3.1 on 2021-04-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocatid',
            field=models.IntegerField(default=0),
        ),
    ]
