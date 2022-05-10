import types
types.ClassType = type

from functools import partial

from twisted.internet import reactor, defer
from twisted.internet.error import CannotListenError
from twisted.internet.protocol import Protocol, ServerFactory, Factory
from twisted.python import log
from twisted.web.client import (
    Agent, RedirectAgent, ProxyAgent, ResponseDone, ResponseFailed,
)
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.web.http_headers import Headers
from twisted.web.server import Site
from twisted.web.iweb import IBodyProducer
from twisted.web.http import PotentialDataLoss
from twisted.web.http import FORBIDDEN, _DataLoss
from twisted.web.proxy import ProxyRequest
from twisted.web.proxy import ProxyClientFactory
from twisted.web.proxy import ProxyClient
from twisted.web.proxy import ProxyClientFactory
from twisted.web.proxy import ProxyClient
from twisted.web.proxy import ProxyClientFactory
from twisted.web.proxy import ProxyClient
from twisted.web.proxy import ProxyClientFactory
from twisted.web.proxy import ProxyClient
