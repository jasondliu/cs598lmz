import mmap
import os
import re
import sys
import zlib
import zmq

from cStringIO import StringIO


class Error(Exception):
    """superclass for all exceptions in this module"""


class UnpicklingError(Error):
    """an error occured while trying to unpickle an object"""


class ConnectionClosed(Error):
    """connection was closed"""


class DataMissing(Error):
    """data is missing, try again later"""


class MessageTooLarge(Error):
    """message is too large (pickle is likely corrupt)"""


class Serializer(object):
    """Base class for serialization with ZeroMQ"""

    def __init__(self, context=None, parent=None):
        self.context = context or zmq.Context.instance()
        self.parent = parent

    def loads(self, buf, parent=None):
        """Load serialized message"""
        return buf

    def dumps(self, msg):
        """returns a serialized message"""
        return msg


class BatchedSerializer(Serializer):
    """Forces multiple
