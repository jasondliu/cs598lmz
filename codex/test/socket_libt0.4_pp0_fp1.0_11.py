import socket
import sys
import threading
import time
import traceback
import unittest

from uuid import uuid4

from cassandra.cluster import Cluster
from cassandra.concurrent import execute_concurrent
from cassandra.query import SimpleStatement
from cassandra.policies import HostDistance
from cassandra.protocol import ConfigurationException

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

from tools.assertions import *
from tools.decorators import since


class ConnectionTests(unittest.TestCase):

    def setUp(self):
        self.cluster = Cluster(protocol_version=3)
        self.session = self.cluster.connect()

    def tearDown(self):
        self.cluster.shutdown()

    def test_default_port(self):
        """
        Test that the default port is used if none is specified
        """

        cluster = Cluster()
        cluster.connect()
