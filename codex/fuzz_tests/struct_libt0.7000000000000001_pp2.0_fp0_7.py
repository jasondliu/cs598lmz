import _struct
import json
import random
import urllib2
import zlib
from binascii import hexlify
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from unittest import TestCase

path.append(abspath(normpath(join(dirname(__file__), '..', '..'))))
import gocardless
from gocardless import error
from gocardless.api import Api, API_ROOT


class TestApi(TestCase):

  def setUp(self):
    self.api = Api('ABC123')

  def test_api_requires_access_token(self):
    try:
      Api()
    except TypeError as e:
      self.assertEqual(str(e), '__init__() takes at least 1 argument (0 given)')
    else:
      self.fail('Expected a TypeError')

  def test_api_requires_string_access_token(self):
    try:
      Api(123)
    except TypeError as e:
