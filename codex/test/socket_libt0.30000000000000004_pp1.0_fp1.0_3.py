import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import UUIDField
from django_extensions.db.models import TimeStampedModel

from . import utils
from . import settings as app_settings


class BaseModel(TimeStampedModel):
    """
    Base model for all models
    """
    uuid = UUIDField(auto=True, primary_key=True)
    user = models.ForeignKey(User, related_name='%(class)s_user',
                             verbose_name=_('user'))

    class Meta:
        abstract = True

