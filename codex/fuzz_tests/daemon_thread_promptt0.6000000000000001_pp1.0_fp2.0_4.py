import threading
# Test threading daemon
import multiprocessing
# Test multiprocessing daemon
import time
import random

import unittest

from tendrl.commons.event import Event
from tendrl.commons.message import ExceptionMessage
from tendrl.commons.message import Message

from tendrl.commons.tests import mock
from tendrl.commons.tests import util


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.msg = Message(
            priority='info',
            publisher="TestPublisher",
            payload={},
            job_id="job_id",
            flow_id="flow_id",
            cluster_id="cluster_id"
        )
        self.exc_msg = ExceptionMessage(
            priority='info',
            publisher="TestPublisher",
            payload={},
            job_id="job_id",
            flow_id="flow_id",
            cluster_id="cluster_id"
        )

    @mock.patch('tendrl.commons.event.Event._run',
                new=util.run
