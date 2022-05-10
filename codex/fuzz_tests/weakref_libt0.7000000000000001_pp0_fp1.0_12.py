import weakref

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _

from freenasUI.freeadmin.models import Model, PathField, UserField
from freenasUI.middleware.notifier import notifier


class SMARTTestInterval(Model):
    smarttest_type = models.CharField(
        max_length=2,
        choices=(('S', _('Short')), ('L', _('Long')), ('C', _('Conveyance')), ('O', _('Offline'))),
    )
    smarttest_dayweek = models.CharField(
        choices=(
            ('*', _('Every Day')),
            ('0', _('Sunday')),
            ('1', _('Monday')),
            ('2', _('Tuesday')),
            ('3', _('Wednesday')),
            ('4', _('Thursday')),
            ('5', _('Friday')),
            ('6',
