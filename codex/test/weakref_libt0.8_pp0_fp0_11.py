import weakref
from logging import getLogger

from django.conf import settings
from django.db import models, transaction
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields.json import JSONField
from ipware.ip import get_ip
from model_utils import FieldTracker
from polymorphic.manager import PolymorphicManager
from polymorphic.query import PolymorphicQuerySet
from polymorphic.showfields import ShowFieldContent
from requests.exceptions import RequestException
from reversion.models import Revision

from kitsune.access.models import Group, GroupUser
from kitsune.kbadge.badge_awarding import award_badges_signal
from kitsune.notifications.tasks import _send_notification
from kitsune.notifications.types import Notification
from kitsune.products.models import Product
from kitsune.sumo.models import ModelBase
from kitsune.sumo.urlresolvers import reverse
