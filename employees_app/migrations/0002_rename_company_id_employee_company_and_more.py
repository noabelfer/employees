# Generated by Django 4.1.5 on 2023-01-29 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='person_id',
            new_name='person',
        ),
    ]
