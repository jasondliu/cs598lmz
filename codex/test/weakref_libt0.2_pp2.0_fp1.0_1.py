import weakref

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _

from . import settings as app_settings
from .models import User
from .utils import get_user_model

