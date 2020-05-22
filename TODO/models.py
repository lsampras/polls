from django.db import models

# Create your models here.

class TODO (models.Model):
    task = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    date = models.DateTimeField('date created')

    def __str__(self):
        return self.task
