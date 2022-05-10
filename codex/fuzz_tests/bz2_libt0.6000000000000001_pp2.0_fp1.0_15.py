import bz2
bz2.BZ2File.fileno = lambda x: x.file.fileno()

import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.error import CannotListenError
from twisted.web.server import Site
from twisted.web.static import File
from txws import WebSocketFactory
from twisted.internet import task
import datetime
import time
import random
from zope.interface import implements
from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
import os
from twisted.internet import threads
from twisted.internet.defer import Deferred, succeed
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.interfaces import IStreamClientEndpoint
import os
from twisted.internet import threads
from twisted.internet.defer import Deferred, succeed
from twisted
