from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    priority = models.IntegerField(default=0)
    task_name = models.CharField(max_length=200)
    time = models.TimeField('%H:%M')
    complete = models.BooleanField()

    def __str__(self):
        return self.task_name

    def to_dict(self):
        return{
            'id': self.id,
            'priority': self.priority,
            'task_name': self.task_name,
            'time': self.time,
            'complete':self.complete,
        }