# Generated by Django 4.2.6 on 2023-11-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_staff', models.IntegerField(verbose_name='Номер сотрудника')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта сотрудника')),
                ('name', models.CharField(max_length=100, verbose_name='Имя сотрудника')),
                ('phone_number', models.IntegerField(verbose_name='Номер сотрудника')),
                ('job', models.CharField(choices=[('Программист', 'Программист'), ('Слесарь', 'Слесарь'), ('Бухглатер', 'Бухглатер')], default='', max_length=100)),
            ],
        ),
    ]
