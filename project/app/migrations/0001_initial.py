# Generated by Django 5.0.1 on 2024-01-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя продукта')),
                ('info', models.TextField(verbose_name='Описание продукта')),
                ('img', models.TextField(verbose_name='ссылка к картинке')),
                ('price', models.IntegerField(verbose_name='стоимость')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shop',
            },
        ),
    ]
