# Generated by Django 4.2 on 2023-05-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_alter_telegramuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия'),
        ),
    ]