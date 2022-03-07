# Generated by Django 4.0.2 on 2022-03-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_aboutusmodel_contactsmodel_imageasset_menu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutusmodel',
            old_name='title',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='contactsmodel',
            old_name='title',
            new_name='key',
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='date_pub',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contactsmodel',
            name='date_pub',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='imageasset',
            name='date_pub',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='date_pub',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='key',
            field=models.CharField(db_index=True, default='', max_length=150, unique=True),
            preserve_default=False,
        ),
    ]