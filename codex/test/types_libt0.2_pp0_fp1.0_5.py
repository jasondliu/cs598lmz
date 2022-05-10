import types
types.ClassType = type

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
                                         ModificationDateTimeField)
from django_extensions.db.models import (TitleSlugDescriptionModel,
                                         TimeStampedModel)

from .managers import (CategoryManager, LinkManager,
                       TaggedItemManager, KeywordManager)


class Category(TitleSlugDescriptionModel):
    """
    A category for grouping links.
    """
    objects = CategoryManager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('title',)

    def __unicode__(self):
        return self.title


