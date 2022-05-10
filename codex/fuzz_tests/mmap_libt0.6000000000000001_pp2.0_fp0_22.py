import mmap
import shutil
import subprocess
import os

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.utils.encoding import smart_unicode
from django.utils.timezone import now
from django.utils.html import escape, strip_tags
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Q

from django_extensions.db.fields import UUIDField
from django_extensions.db.fields.json import JSONField
from django_extensions.
