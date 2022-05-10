import types
types.ModuleType = module

from django.db import models
from django.template import RequestContext
from django.conf import settings
from django.core import exceptions
from django.contrib.auth.models import User, AnonymousUser
from django.views.debug import technical_500_response 
from django.db import connection as django_connection
from django.template.context import Context, RequestContext
from django.test.testcases import TestCase
from django.test.testcases import TestCase as DjangoTestCase
from django.test import Client, utils, TestCase as DjangoTestCase
from django.test.client import MULTIPART_CONTENT, encode_multipart
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test.utils import get_warnings_state, restore_warnings_state
from django.test.signals import setting_changed
from django.utils import unittest
from django.utils.crypto import get_random_string
from django.utils.translation import activate
