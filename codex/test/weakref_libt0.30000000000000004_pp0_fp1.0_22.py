import weakref

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from . import settings
from . import utils
from . import managers
from . import signals
from . import exceptions
from . import validators


@python_2_unicode_compatible
class AbstractBase(models.Model):
    """
    Abstract base class for all models.
    """

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AbstractCategory(AbstractBase):
    """
    Abstract base class for all categories.
    """

    class Meta:
        abstract = True
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True,
        help_text=_('The name of the category.'),
    )

