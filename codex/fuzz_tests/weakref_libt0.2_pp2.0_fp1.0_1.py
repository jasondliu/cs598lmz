import weakref

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import post_save, pre_delete
from django.utils.translation import ugettext_lazy as _

from . import settings as app_settings
from .models import User
from .utils import get_user_model

__all__ = ['User', 'AnonymousUser', 'get_user_model', 'get_user_model_name',
           'get_user_permission_full_codename', 'get_user_permission_codename',
           'get_user_permission_name', 'get_user_permission_content_type',
           'get_user_permission_object', 'get_user_permission_content_type_id',
           'get_user_permission_object_id', 'get_user_permission_id',
           'get_user_permission_pk', 'get_user_permission_natural_key',
           'get_user_permission_natural_key_re
