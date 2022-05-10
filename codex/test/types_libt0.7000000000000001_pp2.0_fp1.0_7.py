import types
types.NoneType = type(None)

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils.html import escape
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify

from tagging.fields import TagField
from tagging.models import Tag
from tagging.utils import get_tag
from tagging_autocomplete.models import TagAutocompleteField
from django_extensions.db.fields import AutoSlugField
from timezones.fields import TimeZoneField
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import force_unicode
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.contrib.sites.models import Site
