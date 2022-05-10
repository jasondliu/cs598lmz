import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

# from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    time = models.DateTimeField()
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField()
    author = models.ForeignKey(User)
    blog = models.ForeignKey(
