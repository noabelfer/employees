import csv
import datetime

import os
from datetime import date

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "employees.settings"

django.setup()

from employees_app.models import *

# new_person = Movie(name="bbb", release_year=2021, duration_in_min=124)


# with open("/Users/noabelfer/Downloads/persons.csv","r") as file:
#     person_file= csv.DictReader(file, delimiter=',')
#     for item in person_file:
#         person=Person(id = int(item["id"]), first_name=item["first_name"],last_name=item["last_name"], personal_email=item["personal_email"],
#                       gender=item["gender"], birth_date=datetime.datetime.strptime(item["birth_date"],"%m/%d/%Y").date())
#         person.save()


# with open("/Users/noabelfer/Downloads/employees.csv","r") as file:
#     employee_file = csv.DictReader(file, delimiter=',')
#     for item in employee_file:
#         employee = Employee(id=int(item["id"]), person_id= item["person_id"], company_id=item["company_id"],
#                             job_title = item["job_title"],
#                             is_current_job=item["is_current_job"].title(),company_email=item["company_email"])
#         employee.save()

# with open("/Users/noabelfer/Downloads/companies.csv","r") as file:
#     company_file = csv.DictReader(file, delimiter=',')
#     for item in company_file:
#         company = Company(id=int(item["id"]), company_name= item["company_name"], country=item["country"],
#                             city = item["city"], address=item["address"],phone_num=item["phone_num"])
#         company.save()

def get_person_name_by_id(person_id: int) -> str:
    person=Person.objects.get(id=person_id)
    print(str(f"{person.first_name},{person.last_name}"))


def get_people_by_age(age: int) -> list:
    today = date.today()
    age_years = datetime.datetime.now().year-age
    person=Person.objects.filter(birth_date__year=age_years)
    print(str(person))

def get_people_cnt_by_gender(gender: str) -> list:
    person=Person.objects.filter(gender=gender)
    return(list(person))

# a=get_people_cnt_by_gender('Male')
# print(a)

def get_companies_by_country(cntry: str) -> list[str]:
    company = Company.objects.filter(country=cntry)
    return(list(company))

def get_company_employees(company_id: int, current_only: bool) -> list[Person]:
    company = Company.objects.get(id=company_id)
    print(company.employee_set.filter(is_current_job = current_only))

# Given person_id, return list of dictionaries that map from company name to job title
#    :param person_id:

def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    p = Person.objects.get(id=person_id).companies.all().values_list('company_name', 'employee__job_title')
    print(dict(p))

# def get_person_jobs(person_id: int) -> list[dict[str, str]]:
#     p = Person.objects.get(id=person_id)
#     print(p.companies.values('company_name'), p.employee_set.values('job_title'))

# def get_person_jobs(person_id: int) -> list[dict[str, str]]:
#     p = Person.objects.filter(id__ne=person_id)
#     print(list(p))


a=get_person_jobs(2)
print(a)


