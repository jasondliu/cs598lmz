import weakref

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import get_user_model


class AbstractBaseProfile(models.Model):
    """
    This is the base model that holds all the generic user information.

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True,
                                related_name='profile')
    slug = models.SlugField(max_length=50, unique=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
   
