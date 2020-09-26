import datetime
from faker import Faker
from django.core.management.base import BaseCommand
from time import sleep
from app.models import User, ActivityPeriod

faker = Faker()

class Command(BaseCommand):
    help = "Save randomly generated activity record values."

    

    def handle(self, *args, **options):
        records = []
        for _ in range(100):
            sleep(0.1)
            kwargs = {
                    
                'user' : User.objects.create(real_name=faker.name(), tz=faker.timezone()),
                'start_time': faker.date_time(),
                'end_time' : faker.date_time(),
                
             }

            record = ActivityPeriod(**kwargs)
            records.append(record)

        ActivityPeriod.objects.bulk_create(records)
        activity = ActivityPeriod.objects.all()

        users = User.objects.all()
        
        for user in users:
            sleep(0.1)
            activity_extend=ActivityPeriod(user= user, start_time=faker.date_time(), end_time=faker.date_time())
            activity_extend.save()
            activity_extend=ActivityPeriod(user= user, start_time=faker.date_time(), end_time=faker.date_time())
            activity_extend.save()
        

        self.stdout.write(self.style.SUCCESS('Activity records saved successfully.'))    

        