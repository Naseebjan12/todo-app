from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_title=models.TextField(max_length=200)
    date=models.DateField()
    description=models.TextField(max_length=500)
    
    def __str__(self):
        return f'{self.task_title} on  {self.date}' 