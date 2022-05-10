import mmap
import os
import tempfile
import uuid

from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError
from kazoo.protocol.states import KazooState
from kazoo.retry import KazooRetry
from kazoo.testing import KazooTestCase
from kazoo.testing.harness import KazooTestHarness
from kazoo.tests.util import random_string, wait_filter

import pytest


class TestKazooRetry(KazooTestCase):
    def test_create_default(self):
        retry = KazooRetry()
        self.assertEqual(retry.delay, 1)
        self.assertEqual(retry.backoff, 2)
        self.assertEqual(retry.max_tries, 10)
        self.assertEqual(retry.max_delay, 60)
        self.assertEqual(retry.jitter, 0.1)
        self.assertEqual(retry.sleep_func, time.sleep)

    def
