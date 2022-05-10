import weakref

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
