import weakref

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from . import utils
from . import settings
from . import signals


class Message(models.Model):
    """
    A private message from user to user
    """
    subject = models.CharField(_("Subject"), max_length=120)
