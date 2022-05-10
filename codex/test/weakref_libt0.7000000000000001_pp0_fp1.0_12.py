import weakref

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _

from freenasUI.freeadmin.models import Model, PathField, UserField
from freenasUI.middleware.notifier import notifier


