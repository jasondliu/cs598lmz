import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from BeautifulSoup import BeautifulSoup

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.encoding import smart_str

from apps.gcd.models import *
from apps.gcd.models.issue import INDEXED
from apps.gcd.models.story import StoryType
from apps.oi.models import *
from apps.oi.covers import get_image_tags_per_page

from apps.gcd.views import get_image_tag

from apps.gcd.migration.utils import *

class Command(BaseCommand):
    args = '<old_site_path> <new_site_path>'
    help = 'Migrates the old site data to the new site data'

    def handle(self, *args, **options):
       
