import socket
import time

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from ella.core.models import Publishable
from ella.core.cache import get_cached_object_or_404
from ella.core.box import Box
from ella.core.conf import core_settings
from ella.core.managers import ListingManager
from ella.core.managers import RelatedManager
from ella.core.managers import PlacementManager
from ella.core.signals import object_rendered
from ella.core.signals import object_displayed
from ella.core.signals import object_displayed_in_listing
from e
