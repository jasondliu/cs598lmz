import types
types.ModuleType.__getattr__ = lambda self, name: self.__dict__.get(name, None)

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

from django_extensions.management.utils import signalcommand

from django_extensions.compat import get_remote_field

try:
    from django.db.transaction import atomic
except ImportError:
    from django.db.transaction import commit_on_success as atomic

class Command(BaseCommand):
    help = "Rename a model's db table"
    args = "[appname] [modelname] [new_table_name]"

