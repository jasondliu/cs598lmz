import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.images import ImageFile
from django.core.files import File

from apps.gcd.models import Publisher, Issue, StoryType, Story, Image
from apps.gcd.models.story import ZERO_ISSUE_VALUES
from apps.gcd.models.cover import ZERO_ISSUE_COVER
from apps.gcd.models.issue import NO_ISBN
from apps.gcd.models.story import NO_PAGE_COUNT
from apps.gcd.models.story import NO_PAGE_COUNT_STRING
from apps.gcd.models.story import NO_PAGE_COUNT
