import gc, weakref
from twisted.internet import defer, reactor, task
from twisted.python import log
from zope.interface import implements

from txampext.multiplex import MultiplexServerProtocol, MultiplexClientProtocol,\
                                IAmpproxyMultiplexFactory

from txampext.sanity import AMPCommandFactory, AMPSanitizer
from txampext import amp

from twisted.internet.protocol import connectionDone

class SimplestProtocol(amp.AMP):
    def connectionMade(self):
        print "Called connectionMade"
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.sendCommand('get_server_time', {})
        self.
