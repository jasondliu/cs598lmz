import weakref

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models

from django.utils.functional import cached_property

from django.core.mail import send_mail

from django.core import validators

from django.utils.encoding import force_text
from django.utils.http import urlquote

from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

