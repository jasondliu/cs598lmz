import socket
import time

from django.utils.encoding import smart_unicode
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save

from drumbeat import messages
from users.models import UserProfile
from richtext.models import RichTextPage
from l10n.models import localize_email
from relationships.models import Relationship

import logging
log = logging.getLogger(__name__)


class MailingListManager(models.Manager):

    def get_queryset(self):
        return super(MailingListManager, self).get_queryset().filter(
            is_active=True)


class MailingList(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_active = models
