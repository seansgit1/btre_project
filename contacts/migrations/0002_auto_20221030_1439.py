# Generated by Django 2.2.28 on 2022-10-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_is',
            new_name='user_id',
        ),
    ]
