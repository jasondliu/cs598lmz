import gc, weakref

from twisted.python import components
from twisted.python.components import registerAdapter

from twisted.persisted import sob

from twisted.internet import defer, reactor

from twisted.application import service
from twisted.application import internet

from twisted.python.failure import Failure

from twisted.enterprise import adbapi

from twisted.python.components import registerAdapter

from twisted.internet import interfaces, protocol, defer
from twisted.internet.defer import Deferred
from twisted.internet.defer import DeferredList
from twisted.internet.defer import DeferredQueue
from twisted.protocols.basic import LineReceiver

from zope.interface import implements

from twisted.python import log

from twisted.internet import reactor

#####
#####
##
##  I'm not sure I'm going to keep this.  It could be useful
##  but it might be better to have all the connections as
##  a single transport, and just have a separate protocol for each
##  connection
##
#####
#####


class Connection(LineReceiver):

    def __init
