import gc, weakref
from twisted.internet import defer
from twisted.python import log

class TimeoutError(Exception):
    """
    The entity we were waiting for did not appear in the allotted time.
    """
    def __init__(self, name, timeout):
        self.name = name
        self.timeout = timeout
    def __str__(self):
        return "<TimeoutError: %s didn't appear within %s>" % (self.name,
                                                               self.timeout)


class Timeout(object):
    """
    A wrapper that calls a given Deferred after a certain time.
    """
    def __init__(self, reactor, timeout, deferred):
        self.reactor = reactor
        self.timeout = timeout
        self.deferred = deferred

    def start(self):
        self.callID = self.reactor.callLater(self.timeout,
                                             self.deferred.errback,
                                             TimeoutError(self.deferred,
                                                          self.timeout))

    def stop(self):
        if self.callID.active
