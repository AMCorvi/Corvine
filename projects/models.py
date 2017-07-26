from django.db import models
from datetime import datetime

# Utilize the same tags structure as the Blog Model
from blog.models import Tag


#  Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=40)
    img_url = models.URLField(max_length=100)
    repo_url = models.URLField(max_length=100)
    project_url = models.URLField(max_length=100)
    attribution_date = models.DateTimeField(name='date published',  default=datetime.now())

    description = models.CharField(max_length=500)
    is_https = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)



    # 'technologies' is being used to make do as a tag. Note that it will take on the following format:
    #  e.g. (" reactjs, nodejs, mocha, chai, python, django")
    # This field should therefore be sorted using the 'str.split()' method.
    technologies =  models.CharField(max_length=100)

    def __str__(self):
        return self.project_name
