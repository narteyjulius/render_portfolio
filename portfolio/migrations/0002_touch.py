# Generated by Django 3.2.4 on 2021-07-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Touch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
