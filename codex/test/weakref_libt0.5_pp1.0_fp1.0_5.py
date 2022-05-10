import weakref

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

from .fields import JSONField
from .managers import (
    ActionManager,
    FollowManager,
    MentionManager,
    NotificationManager,
    StreamManager,
)
from .registry import registry
from .utils import get_target_model, get_target_model_name, get_target_model_pk


class Action(models.Model):
    """
    Records an action taken by a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="actions", verbose_name=_("User"), on_delete=models.CASCADE)
