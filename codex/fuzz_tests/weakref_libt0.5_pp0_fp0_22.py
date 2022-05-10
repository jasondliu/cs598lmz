import weakref
import threading
import time
import copy
import logging
import socket

from zope.interface import implements

from twisted.internet import defer, threads, task, error
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.interfaces import IConsumer
from twisted.python.failure import Failure
from twisted.python.threadable import isInIOThread

from txzookeeper.client import ZookeeperClient
from txzookeeper.retry import RetryClient
from txzookeeper.interfaces import IZooKeeperClient
from txzookeeper.utils import flatten_tree

from txzookeeper.protocol import ZOOKEEPER_READONLY

from txzookeeper.tests.utils import ZookeeperServerHarness


class _TestingProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.data = []
        self.closed = False

    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason):

