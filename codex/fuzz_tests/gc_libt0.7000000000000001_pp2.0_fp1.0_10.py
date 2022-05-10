import gc, weakref, sys, traceback
from cStringIO import StringIO

from twisted.python import log
from twisted.internet import defer, reactor
from twisted.trial import unittest
from txamqp import spec, client, queue, contents
from txamqp.protocol import AMQClient
from txamqp.client import TwistedDelegate
from txamqp.queue import TimeoutDeferredQueue
from txamqp.testlib import TestBase

from txamqp.queue import *


class QueueTests(unittest.TestCase):

    def test_basic_consume(self):
        q = Queue()

        def got_message(*args, **kwargs):
            pass

        q.basic_consume(got_message, no_ack=True)
        self.assertEquals(len(q.channel.callbacks), 1)
        self.assertEquals(q.channel.callbacks.values()[0], got_message)

    def test_basic_cancel(self):
        q = Queue()
        q.channel.delivery_
