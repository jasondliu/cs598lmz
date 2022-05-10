import weakref
import socket
import errno

from datetime import datetime
from twisted.internet import reactor, interfaces
from twisted.internet.defer import Deferred, CancelledError, fail, succeed
from twisted.internet.task import LoopingCall
from twisted.python import threadable, log
from zope.interface import implementer

from . import base
from . import buddyset
from . import database
from . import listmixin
from . import net
from . import ploop
from . import relay
from . import sarien
from . import util

class DeadException(Exception):
    pass

def ErrnoToString(e):
    for name in dir(errno):
        if getattr(errno, name) == e:
            return name

class StubRelay(object):
    def __init__(self, addr, username):
        self.addr = addr
        self.username = username

    def logout(self):
        pass

class ProxyRelay(object):
    def __init__(self, addr, username, client):
        self.addr = addr
       
