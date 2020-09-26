from django.db import models

class User(models.Model):
    id = models.CharField(max_length=10,blank=True, primary_key=True)
    real_name= models.CharField(max_length=20,  blank=True)
    tz= models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person_activity',  blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)


