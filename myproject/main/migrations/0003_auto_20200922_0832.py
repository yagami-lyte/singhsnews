# Generated by Django 3.1 on 2020-09-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(),
        ),
    ]
