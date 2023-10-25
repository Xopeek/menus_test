# Generated by Django 4.2.6 on 2023-10-25 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('long_name', models.CharField(max_length=256, verbose_name='Verbose_name')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('link', models.CharField(max_length=256, verbose_name='Link')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory', verbose_name='Категория')),
                ('parent_item', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='menu.menu', verbose_name='Parent element')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
            },
        ),
    ]
