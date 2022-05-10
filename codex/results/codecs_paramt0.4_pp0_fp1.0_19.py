import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
from django.utils.text import slugify

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.comments.models import Comment
from django.contrib.comments.managers import CommentManager
from django.contrib.comments.signals import comment_was_posted

from django.utils.translation import ugettext_lazy as _

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.views import flatpage

from django.contrib.redirects.models import Redirect
from django.contrib.redirects.middleware
