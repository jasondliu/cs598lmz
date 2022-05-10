import select
import socket
import sys
import traceback

from datetime import datetime
from datetime import timedelta
from dateutil import tz

from . import configuration
from . import constants
from . import file_operations
from . import log
from . import net_utilities
from . import results
from . import system_tools
from . import utils


# Get and set the logger for this module.
logger = log.get_logger(__name__)


class TestCase(object):
    """
    TestCase class for running a single test case.
    """

    def __init__(self, test_case_id, test_case):
        """
        Initialize the TestCase object.

        :param test_case_id: ID of the test case.
        :type test_case_id: str
        :param test_case: Test case object.
        :type test_case: dict
        """

        # Set the test case ID.
        self.test_case_id = test_case_id

        # Set the test case object.
        self.test
