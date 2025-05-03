from django.db import models
from django.utils.text import slugify

# Create your models here.


JOB_TYPE = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
)


def image_upload_to(instance, filename):
    name, ext = filename.split('.')
    return 'jobs/{}.{}'.format(instance.id, ext)

class Job(models.Model):
    title = models. CharField(max_length=100) # column
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models. IntegerField(default=1)
    salary = models. IntegerField(default=0)
    experience = models. IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='jobs')
    image = models.ImageField(upload_to=image_upload_to)


    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Job.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


    class Apply(models.Model):
        job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply')
        name = models.CharField(max_length=100)
        email = models.EmailField()
        website = models.URLField(blank=True, null=True)
        cv = models.FileField(upload_to='apply/cvs/')
        cover_letter = models.TextField(max_length=1000, blank=True, null=True)
        applied_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.name} - {self.job.title}"