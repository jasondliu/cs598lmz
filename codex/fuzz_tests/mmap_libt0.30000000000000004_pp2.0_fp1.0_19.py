import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib2

import common
import test_utils


class TestCase(test_utils.BaseTest):
  """Base class for all test cases."""

  def __init__(self, *args, **kwargs):
    super(TestCase, self).__init__(*args, **kwargs)
    self.test_data = None
    self.test_data_path = None
    self.test_data_url = None
    self.test_data_size = None
    self.test_data_sha1 = None
    self.test_data_sha256 = None
    self.test_data_sha512 = None
    self.test_data_md5 = None
    self.test_data_filename = None

  def setUp(self):
    super(TestCase, self).setUp()
    self.test_data = None
    self.test_data_path = None
    self.test_data_url = None
    self.test
