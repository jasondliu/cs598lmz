import mmap
import os
import pickle
import random
import re
import shutil
import string
import subprocess
import sys
import tempfile
import time
import unittest

from . import (
    DEFAULT_TEST_TIMEOUT,
    LdapTestCase,
    LdapTestCaseMeta,
    LdapTestCaseMetaClass,
    LdapTestConnection,
    LdapTestServer,
    LdapTestServerFactory,
    LdapTestServerManager,
    LdapTestServerPool,
    TestCase,
)

if sys.version_info[0] >= 3:
    unicode = str


class TestLdapTestCaseMeta(TestCase):
    def test_init(self):
        ldap_test_case_meta = LdapTestCaseMeta(
            unicode('test_ldap_test_case_meta'), (TestCase,), {}
        )
        self.assertEqual(ldap_test_case_meta.ldap_test_case_class, LdapTestCase)


class
