import gc, weakref, sys

from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from . import settings
from .utils import get_image_dimensions, get_image_ratio

from .managers import ImageManager

from . import signals

from . import utils

from . import conf

from .tasks import process_image_upload

from . import exceptions

from . import fields


class BaseImage(models.Model):
    """
    Base class for images.
    """
    image = fields.ImageField(
        _('image'),
        upload_to=conf.IMAGE_UPLOAD_TO,
        max_length=255,
        blank=True,
