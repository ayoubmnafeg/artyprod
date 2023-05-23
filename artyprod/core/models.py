from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Service(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='media/services', blank=True, null=True)
    
    def __str__(self):
        return self.type


class Project_tag(models.Model):
    tag = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag


class Client(models.Model):
    email = models.EmailField()
    photo = models.ImageField(upload_to='media/account_pdp', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return str(self.user)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='media/staff', blank=True, null=True)
    in_url = models.URLField(blank=True, null=True, default='https://www.linkedin.com/')
    site_url = models.URLField(blank=True, null=True)
    
    REQUIRED_FIELDS = ['name', 'job_title', 'description']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('IP', 'In Progress'),
        ('IR', 'In Review'),
        ('CL', 'Cancelled')
    ]
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='media/projects', blank=True, null=True)
    tags = models.ManyToManyField('Project_tag')
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    responsibles = models.ManyToManyField(Staff, related_name='staff')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    
    REQUIRED_FIELDS = ['name', 'description', 'tags']
    
    def __str__(self):
        return self.project_name
