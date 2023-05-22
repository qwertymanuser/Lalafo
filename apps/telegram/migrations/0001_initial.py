# Generated by Django 4.2 on 2023-05-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=100, verbose_name='ID пользователя')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('chat_id', models.CharField(max_length=100, verbose_name='Чат ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Пользователь телеграма',
                'verbose_name_plural': 'Пользователи телеграма',
            },
        ),
    ]
