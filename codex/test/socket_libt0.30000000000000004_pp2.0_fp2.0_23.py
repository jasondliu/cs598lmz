import socket

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from . import utils
from . import settings as app_settings


class Server(models.Model):
    """
    A server to be monitored.
    """
    name = models.CharField(_('name'), max_length=255)
    hostname = models.CharField(_('hostname'), max_length=255)
    port = models.PositiveIntegerField(_('port'), default=22)
    username = models.CharField(_('username'), max_length=255)
    password = models.CharField(_('password'), max_length=255, blank=True)
    private_key = models.TextField(_('private key'), blank=True)
    private_key_passphrase = models.CharField(_('private key passphrase'), max_length=255, blank=True)
    enabled = models.BooleanField(_('enabled'), default=True)
