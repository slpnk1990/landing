# Generated by Django 4.0.2 on 2022-03-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_menu_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutusmodel',
            options={'ordering': ['id'], 'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='contactsmodel',
            options={'ordering': ['id'], 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'ordering': ['id'], 'verbose_name': 'Домашняя страница', 'verbose_name_plural': 'Домашняя страница'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['id'], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
    ]