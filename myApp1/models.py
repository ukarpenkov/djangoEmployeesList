from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

class Worker(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    position = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='workers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"