import select
import socket
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import connection
from django.db import models
from django.db.models import Q
from django.db.models import Sum
from django.db.models.signals import post_save
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

from django_statsd.clients import statsd

from celery.task import task
