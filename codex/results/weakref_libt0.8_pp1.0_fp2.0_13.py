import weakref

from django.conf import settings
from django.db import connection

from django.db.models import signals
from django.db.models.fields import FieldDoesNotExist

from django.db.models import get_model

from django.http import HttpResponse
from django.utils import simplejson

from django.utils.translation import ugettext as _

from email.mime.text import MIMEText

from google.appengine.api.labs import taskqueue

from djangoappengine.db.proxies import ListFieldProxy, ModelListFieldProxy
from djangoappengine.db.proxies import ListProperty, ModelListProperty
from djangoappengine.db.utils import email_to_mime

class Background(object):
    """ Decorator that allows to define a function as background task. """

    def __init__(self, callback=None, queue='default', deferred=False, retry=True):
        self.callback = callback
        self.queue = queue
        self.deferred = deferred
        self.
