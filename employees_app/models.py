import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(db_column="company_name", max_length=256, null=False, blank=False)
    country = models.CharField(db_column='country',max_length=128, null=False, blank=False)
    city = models.CharField(db_column='city', max_length=128, null=False, blank=False)
    address = models.CharField(db_column='address',max_length=256, null=False, blank=False)
    phone_num = models.CharField(db_column='phone_num', max_length=16)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'companies'

class Person(models.Model):
    first_name = models.CharField(db_column="first_name", max_length=256, null=False, blank=False)
    last_name = models.CharField(db_column="last_name", max_length=256, null=False, blank=False)
    personal_email = models.EmailField(db_column="personal_email")
    male = 'male'
    female = 'female'
    agender = 'agender'
    polygender = 'polygender'
    Genderfluid = 'genderfluid'
    Bigender = 'bigender'

    GENDER_CHOICES = [(male, 'male'),(female, 'female'),(agender,'agender'),(polygender,'polygender'),(Genderfluid,'genderfluid'),(Bigender,'bigender')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=16)
    birth_date = models.DateField(db_column='birth_date', validators=[MinValueValidator(datetime.datetime(1900, 1, 1, 0, 0)),MaxValueValidator(datetime.datetime.now)])
    companies = models.ManyToManyField(Company, through='Employee')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'persons'



class Employee(models.Model):
    person = models.ForeignKey('Person', on_delete=models.RESTRICT)
    company = models.ForeignKey('Company', on_delete=models.RESTRICT)
    job_title = models.CharField(db_column='job_title', max_length=256,null=False,blank=False)
    is_current_job = models.BooleanField(db_column='is_current_job', null=False, blank=False)
    company_email = models.EmailField(db_column='company_email')

    def __str__(self):
        return (f"{self.person}, {self.company}")

    class Meta:
        db_table = 'employees'









