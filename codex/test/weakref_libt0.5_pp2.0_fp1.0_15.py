import weakref
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.db.models import signals
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.contrib.comments.signals import comment_was_posted
from django.contrib.comments.models import Comment
from django.contrib.auth.models import User
from django.template import Context, Template
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
