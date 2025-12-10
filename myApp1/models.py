from django.db import models

class Worker(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    position = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"