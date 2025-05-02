from django.db import models

# Create your models here.


JOB_TYPE = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
)

class Job(models.Model):
    title = models. CharField(max_length=100) # column
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models. IntegerField(default=1)
    salary = models. IntegerField(default=0)
    experience = models. IntegerField(default=1)

    def __str__(self):
        return self.title