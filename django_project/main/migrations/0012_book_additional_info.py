# Generated by Django 3.2.8 on 2021-11-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_book_numofpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='additional_info',
            field=models.JSONField(default={}),
        ),
    ]
