import mmap
import os.path
import sys
import gc

import pika
import pika.credentials
import pika.exceptions

from . import _utils as utils
from . import _utils
from . import _compat
from . import __version__

import psycopg2
import psycopg2.extensions

import logging
import time

try:
    pass
except:
    pass


class ConfigError(Exception):
    pass


class ConsumerCancelled(Exception):
    pass


class EmptyQueue(Exception):
    pass


class AlreadyConsuming(Exception):
    pass


class InvalidGroupError(Exception):
    pass


class ResetParameter(object):

    def __init__(self):
        pass


class CallbackRegistry(object):

    def __init__(self):
        self.callbacks = []

    def add(self, callback, one_shot=False):
        self.callbacks.append((callback, one_shot))

    def process(self, *args, **kwargs):
        for callback, one_
