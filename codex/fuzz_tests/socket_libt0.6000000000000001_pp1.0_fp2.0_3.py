import socket
import sys
import time
import threading
import unittest

from b3.fake import fakeConsole, joe, simon
from b3.parsers.iourt42 import Iourt42Parser
from b3.parsers.iourt43 import Iourt43Parser
from b3.update import B3version
from b3.config import XmlConfigParser
from b3.plugins.poweradminurt import PoweradminurtPlugin
from tests import logging_disabled


class PoweradminurtTestCase(unittest.TestCase):
    """
    Test case that is suitable for testing PoweradminurtPlugin
    """
    @classmethod
    def setUpClass(cls):
        with logging_disabled():
            from b3.parsers.q3a.abstractParser import AbstractParser
            from b3.fake import FakeConsole
            AbstractParser.__bases__ = (FakeConsole,)
            # Now parser inheritance hierarchy is :
            # Iourt42Parser -> abstractParser -> FakeConsole -> Parser

    def setUp(self):
        # create a Iourt42 parser
        self.
