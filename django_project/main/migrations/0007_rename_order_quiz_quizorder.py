# Generated by Django 3.2.8 on 2021-11-01 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211101_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='order',
            new_name='quizOrder',
        ),
    ]