import signal
# Test signal.setitimer to make sure it works on this system
try:
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
except ValueError:
    raise SystemExit("Signal setitimer error, exiting")

import sys
import time
from glob import glob

from zope.interface import implements

from twisted.internet import task
from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet import endpoints
from twisted.internet.protocol import Protocol
from twisted.internet.interfaces import IProtocol
from twisted.internet.error import ReactorNotRunning
from twisted.internet.defer import Deferred
from twisted.internet.defer import succeed
from twisted.internet.defer import inlineCallbacks
from twisted.internet.defer import returnValue

from twisted.python import log
from twisted.python.log import ILogObserver
from twisted.python.log import FileLogObserver
from twisted.python.failure import Failure
from twisted.python.runtime import seconds
from twisted.python.procutils import which

from twisted.conch.
