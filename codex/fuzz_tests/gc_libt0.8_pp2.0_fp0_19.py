import gc, weakref
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignal as Signal

import qt4reactor
qt4reactor.install()

from twisted.internet import defer
from twisted.internet.defer import succeed
from twisted.internet.protocol import ClientCreator
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet import reactor

from autobahn.websocket import WebSocketClientFactory, \
                               WebSocketClientProtocol, \
                               connectWS

from twisted.internet.defer import Deferred
from twisted.internet.endpoints import TCP4ClientEndpoint

class MyFrame(QtGui.QFrame):

    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setMinimumSize(300, 300)
        self.setVisible(True)

    def mousePressEvent(self, ev):
        print "widget {} clicked".format(self)

class MyClientProtocol(WebSocketClientProtocol
