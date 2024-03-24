from django.db import models
import uuid

# Create your models here.
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-Time', 'Full Time'),
        ('Part-Time', 'Part Time'),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=200, null=False)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    location = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=False)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title