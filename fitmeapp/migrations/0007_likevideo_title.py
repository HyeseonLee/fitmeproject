# Generated by Django 2.2.1 on 2019-08-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitmeapp', '0006_auto_20190809_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='likevideo',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
