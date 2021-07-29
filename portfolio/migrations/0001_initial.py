# Generated by Django 3.2.4 on 2021-07-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.CharField(blank=True, max_length=200)),
                ('intor_image', models.ImageField(blank=True, upload_to='')),
                ('skill_name', models.CharField(blank=True, max_length=50)),
                ('profile', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('about', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
