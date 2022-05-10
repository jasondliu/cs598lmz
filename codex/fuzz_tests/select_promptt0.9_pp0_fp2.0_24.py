import select
# Test select.select for a client and a server.
# Server:  run python3 select.py 127.0.0.1
# Client:  run python3 select.py
# (Implementation is incomplete:  not all attributes are implemented!)

from __future__ import print_function
from __future__ import absolute_import
from builtins import zip
from builtins import str
from builtins import range
from past.utils import old_div
from builtins import object
from random import choice,randrange
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread,Lock
from operator import attrgetter
from time import time,sleep
from os import strerror

from Pyro4.errors import ConnectionClosedError


class SelectClient(object):
    def __init__(self, s, verbose_errors=False):
        self.s=s
        self.closing=False
        self.tid=0
        self.verbose_errors=verbose_errors
    def fileno(self):
        return self.s.fileno()
    def close(self
