import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.conf import settings
from django.utils.text import slugify
from django.utils.html import strip_tags

from bs4 import BeautifulSoup

from ...models import *

import re
import os
import json
import requests
import datetime
import time
import random
import string
import urllib
import urllib2
import urlparse
import traceback

from optparse import make_option

class Command(BaseCommand):
    help = 'Import data from the old site'
    option_list = BaseCommand.option_list + (
        make_option('--file',
            action='store',
            dest='file',
            default=False,
            help='Import from a file'),
        make_option('--url',
            action='store',
            dest='url',
           
