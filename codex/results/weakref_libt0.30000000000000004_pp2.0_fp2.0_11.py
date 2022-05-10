import weakref

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from .managers import (
    CategoryManager,
    CategoryTranslationManager,
    CategoryTranslationProxyManager,
    ProductManager,
    ProductTranslationManager,
    ProductTranslationProxyManager,
)


class Category(TimeStampedModel):
    """
    A category of products.
    """

    name = models.CharField(max_length=255, verbose_name=_("name"))
    slug = AutoSlugField(populate_from="name", unique=True, verbose_name=_("slug"))
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("parent")
    )
    description = models.TextField(blank=True, verbose_name=_("description
