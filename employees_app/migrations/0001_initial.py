# Generated by Django 4.1.5 on 2023-01-29 12:17

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(db_column='company_name', max_length=256)),
                ('country', models.CharField(db_column='country', max_length=128)),
                ('city', models.CharField(db_column='city', max_length=128)),
                ('address', models.CharField(db_column='address', max_length=256)),
                ('phone_num', models.CharField(db_column='phone_num', max_length=16)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(db_column='job_title', max_length=256)),
                ('is_current_job', models.BooleanField(db_column='is_current_job')),
                ('company_email', models.EmailField(db_column='company_email', max_length=254)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='employees_app.company')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=256)),
                ('last_name', models.CharField(db_column='last_name', max_length=256)),
                ('personal_email', models.EmailField(db_column='personal_email', max_length=254)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('agender', 'agender'), ('polygender', 'polygender'), ('genderfluid', 'genderfluid'), ('bigender', 'bigender')], max_length=16)),
                ('birth_date', models.DateField(db_column='birth_date', validators=[django.core.validators.MinValueValidator(datetime.datetime(1900, 1, 1, 0, 0)), django.core.validators.MaxValueValidator(datetime.datetime.now)])),
                ('companies', models.ManyToManyField(through='employees_app.Employee', to='employees_app.company')),
            ],
            options={
                'db_table': 'persons',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='employees_app.person'),
        ),
    ]
