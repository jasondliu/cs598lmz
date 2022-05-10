import weakref

from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory

from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet.endpoints import TCP4ServerEndpoint

from twisted.internet.defer import Deferred
from twisted.internet.defer import DeferredList
from twisted.internet.defer import inlineCallbacks

from twisted.python.failure import Failure

from twisted.web.client import Agent
from twisted.web.client import readBody

from twisted.web.http_headers import Headers

from twisted.web.iweb import IBodyProducer

from twisted.web.server import Site
from twisted.web.server import NOT_DONE_YET

from twisted.web.resource import Resource

from twisted.web.http import HTTPChannel
from twisted.web.http import HTTPClient
from twisted.web.http import Request

from twisted.web.http_headers import Headers

from twisted.web.client import Agent
from twisted.web.client import read
