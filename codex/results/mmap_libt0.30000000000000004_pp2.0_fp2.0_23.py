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
from BeautifulSoup import Tag

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Q

from pyquery import PyQuery as pq

from apps.gcd.models import Issue, Story, StoryType, INDEXED
from apps.gcd.models.story import STORY_TYPES
from apps.gcd.models.cover import ZOOM_SMALL, ZOOM_MEDIUM
from apps.gcd.models.image import ImageType
from apps.gcd.models.issue import INDEXED_TYPES
from apps.gcd.models.publisher import Publisher
from apps.gcd.models.series import Series
from apps.gcd.models.brand import Brand
from apps.gcd.models.indicia_
