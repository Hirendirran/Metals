import csv
from django.core.management.base import BaseCommand
from prices.models import MetalPrice
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('prices.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                MetalPrice.objects.create(
                    date=datetime.strptime(row['Date'], '%d-%m-%Y'),
                    gold=row['Gold_INR_per_gram'],
                    silver=row['Silver_INR_per_gram'],
                    platinum=row['Platinum_INR_per_gram'],
                    diamond=row['Diamond_INR_per_carat']
                )
