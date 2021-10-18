from django.db import models
from datetime import timedelta

# Create your models here.
class timediff(models.Model):
    start_time=models.DateTimeField(null=True, blank=True)
    end_time=models.DateTimeField(null=True, blank=True)
    

    ###Could be called from views.py
    def calculate_timediff(self, **kwargs):
        
        if(self.end_time < self.start_time):# Invalid Input
            return 0;
        else:
            self.time_difference = self.end_time - self.start_time
            self.seconds = self.time_difference.total_seconds()
            return 1;
       


