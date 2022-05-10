import select
import sys
import time
import traceback

import pytest

from . import util
from .util import skip_if_broken_multiprocessing_spawn

from .test_basic import BasicTestCase
from .test_basic import BasicTests
from .test_basic import run_test


class ProcessTestCase(BasicTestCase):

    def setUp(self):
        self.manager = multiprocessing.Manager()

    def tearDown(self):
        self.manager.shutdown()


class _TestProcess(multiprocessing.Process):

    def __init__(self, testcase):
        multiprocessing.Process.__init__(self)
        self.testcase = testcase

    def run(self):
        self.testcase.run_in_process(self.testcase)


class ProcessSpawnTests(ProcessTestCase):

    @classmethod
    def _test_body(cls, conn):
        BasicTests.test_0_empty_list(conn)
