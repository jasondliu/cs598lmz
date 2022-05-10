import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from optparse import make_option

from apps.gcd.models import *
from apps.gcd.models.cover import ZOOM_SMALL, ZOOM_MEDIUM, ZOOM_LARGE
from apps.gcd.models.story import STORY_TYPES
from apps.gcd.models.image import IMAGE_TYPES
from apps.gcd.models.issue import INDEXED
from apps.gcd.models.publisher import Publisher
from apps.gcd.models.brand import Brand
from apps.gcd.models.series import Series
from apps.gcd.models.issue import Issue
from apps.gcd.models.story import Story
