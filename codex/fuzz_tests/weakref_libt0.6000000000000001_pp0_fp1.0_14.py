import weakref

from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.db.models.query import QuerySet
from django.utils import six
from django.utils.encoding import smart_text
from django.utils.functional import curry, lazy
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField,
)

from jalapeno.models import (
    ActiveModel, ActiveManager, ActiveQuerySet, ActiveState,
)

from .conf import app_settings
from .exceptions import (
    CannotChangeActiveStateException, CannotSetActiveStateException,
    CannotSetInactiveStateException,
)


class ActiveQuerySetMixin(object):

    def _clone(self, klass=None, setup=False, **kwargs):
        kwargs.pop('active', None)
        kwargs.pop('active_state', None)
        kwargs
