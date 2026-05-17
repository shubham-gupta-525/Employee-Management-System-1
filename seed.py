import os
import django
import random
from faker import Faker
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ems_main.settings')
django.setup()

from employee.models import Employee

fake = Faker()

roles = [
    "Software Engineer",
    "HR Manager",
    "Accountant",
    "Team Lead",
    "Backend Developer",
    "Frontend Developer",
    "Data Analyst",
    "QA Engineer",
    "Project Manager",
    "DevOps Engineer"
]

for i in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()

    Employee.objects.create(
        first_name=first_name,
        last_name=last_name,
        role=random.choice(roles),
        phone=fake.phone_number()[:15],
        email=f"{first_name.lower()}.{last_name.lower()}{i}@company.com",
        salary=Decimal(random.randint(30000, 120000)),
        hire_date=fake.date_between(start_date='-5y', end_date='today')
    )

print("100 Employees Added Successfully!")