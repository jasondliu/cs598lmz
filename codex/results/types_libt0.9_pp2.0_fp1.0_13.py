import types
types.ModuleType(
    name='%s.models' % app_label,  # This includes the app label.
)""" % { 'app_label': app_label, 'module_dir': os.path.join(app_dir_name, 'models') }

test_base_template = """from django.test import TestCase
from datetime import datetime
from django.db.utils import DataError

from .base import BaseTestCase
from .api_base import ApiBaseTestCase

from %s.models import *

# Put your test cases here.
""" % app_label

test_api_base_template = """from %s.tests.base import BaseTestCase
from rest_framework.test import APIClient
from django.urls import reverse
from %s.models import *

from rest_framework import status
import types
from operator import attrgetter

from django.db.models import Max

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
