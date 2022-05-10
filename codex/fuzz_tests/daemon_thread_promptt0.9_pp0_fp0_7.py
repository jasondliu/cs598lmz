import threading
# Test threading daemon
import sched
# Test POSIX thread.
import calendar
import math
import readline
import sys
import weakref

from serval.nonportable import posix
from serval import utils
from serval_controller import process
from serval_controller import serval_instance
from serval_tests import test_base
from serval_tests import time_accurate_thread
from serval_tests import test_runner_util


@test_base.skip("Combination with other tests will not enable CPU.")
class ControlledProcessingTest(test_base.TestBase):
    """ControlledProcessingTest contains unit tests for the CodeShack CPU
    feature."""

    @classmethod
    def setUpClass(cls):
        super(ControlledProcessingTest, cls).setUpClass()
        cls.serval = serval_instance.ServalInstance(
            enable_nat=True, enable_voltage_control=True)

    def stop_core(self, core):
        """Stop the core and make sure it stops."""
        process.ProcessRunner(
            self._
