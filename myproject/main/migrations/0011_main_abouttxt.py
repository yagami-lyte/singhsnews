# Generated by Django 3.1 on 2021-04-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210420_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default=''),
        ),
    ]
