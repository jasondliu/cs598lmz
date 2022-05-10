import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.db import models
from django.db.models import Q

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.db import models
from django.db.models import Q

from django.template.defaultfilters import slugify

from
