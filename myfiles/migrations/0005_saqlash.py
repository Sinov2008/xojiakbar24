# Generated by Django 4.1.4 on 2022-12-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_murojaat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saqlash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=80)),
            ],
        ),
    ]