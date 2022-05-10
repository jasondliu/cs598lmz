import weakref

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django_extensions.db.models import TimeStampedModel

from dpaste.highlight import pygmentize, LEXER_DEFAULT, LEXER_AUTO

from .managers import SnippetManager


class Snippet(TimeStampedModel):
    """Snippet model."""

    objects = SnippetManager()
