import socket

import mock
from testtools import matchers

from taskflow import engines
from taskflow.patterns import linear_flow as lf
from taskflow.types import failure
from taskflow.types import futures
from taskflow import utils
from taskflow.utils import misc
from taskflow.utils import threading_utils as tu
from taskflow.utils import uuidutils

from taskflow.tests import utils as test_utils
from taskflow.tests import utils


class TestExecutor(utils.EngineTestBase):

    def test_default_executor(self):
        flow = lf.Flow("test-default-executor")
        flow.add(utils.DummyTask())
        engine = self._make_engine(flow)
        engine.run()
        self.assertIsInstance(engine._executor, futures.GreenThreadPoolExecutor)

    def test_executor_type(self):
        flow = lf.Flow("test-executor-type")
        flow.add(utils.DummyTask())
