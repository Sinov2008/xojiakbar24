# Generated by Django 4.1.4 on 2022-12-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_servise_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('gmail', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
