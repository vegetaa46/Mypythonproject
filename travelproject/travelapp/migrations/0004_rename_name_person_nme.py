# Generated by Django 4.2.3 on 2023-09-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_nme_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='nme',
        ),
    ]