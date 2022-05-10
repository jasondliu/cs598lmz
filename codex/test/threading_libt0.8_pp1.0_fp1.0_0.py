import threading
threading.Thread.daemon = lambda self, flag: None

from django.utils.translation import ugettext as _

from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.db.models import permalink
from django.template.loader import render_to_string

from submission.models import Submission
from judge.models import Profile, Language
from judge.poster import enqueue


class Grader(models.Manager):
    def get_query_set(self):
        return super(Grader, self).get_query_set().filter(allow_grading=True)


class Problem(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=30)
    allow_grading = models.BooleanField(default=False)
    code = models.CharField(max_length=10, blank=True)
    grader = Grader()
