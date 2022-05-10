import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import urllib
import urllib2
import urlparse

from django.conf import settings
from django.core import management
from django.core.urlresolvers import reverse
from django.db import connection
from django.db.models import loading
from django.test import _doctest as doctest
from django.test.client import Client
from django.test.utils import setup_test_environment, teardown_test_environment
from django.utils.encoding import smart_str
from django.utils.functional import curry
from django.utils.itercompat import is_iterable
from django.utils.unittest import TestCase

from .models import Article, Person, Tag

# The password for the fixture data user.
PASSWORD = "password"

# The modified time of a file containing PASSWORD, as a string.
FILE_MTIME = "2006-06-16T11:20:37
