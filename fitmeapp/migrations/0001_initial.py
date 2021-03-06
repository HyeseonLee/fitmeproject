# Generated by Django 2.1.8 on 2019-08-08 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorys', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlId', models.CharField(max_length=100)),
                ('majorTitle', models.CharField(max_length=100)),
                ('subTitle', models.CharField(max_length=100)),
                ('cateName', models.CharField(max_length=100)),
                ('cateDetailName', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cate_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitmeapp.Category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
