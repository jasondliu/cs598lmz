import mmap
import os
import re
import socket
import struct
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import unittest

# pip module (optional, for testing)
try:
    import dns
except ImportError:
    dns = None

import dnspython.dns
import dns.zone

#
# TestConstants
#

class TestDnsPythonConstants(object):
    def __init__(self, config):
        self.config = config


#
# TestBase
#

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = TestConfig()
        cls.constants = TestConfigConstants(cls.config)
        # If we don't explicitly set the DNSSEC key module, the built-in
        # openssl library will be used (if available), when creating test
        # keys. This can be useful for debugging key creator issues.
        cls.dnssec_keys_module = None
