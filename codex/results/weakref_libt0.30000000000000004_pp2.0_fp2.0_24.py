import weakref

from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField)
from django_extensions.db.models import TimeStampedModel

from . import settings as app_settings
from .utils import get_user_model


class UserProfile(TimeStampedModel):
    """
    A user profile.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    slug = AutoSlugField(populate_from='username', unique=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=
