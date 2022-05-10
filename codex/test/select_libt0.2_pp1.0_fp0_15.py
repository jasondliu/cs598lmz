import select
import socket
import sys
import time
import traceback
import urllib
import urlparse
import xml.dom.minidom

from cStringIO import StringIO
from xml.dom.minidom import parseString

from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList
from twisted.internet.protocol import Protocol
from twisted.internet.ssl import ClientContextFactory
from twisted.python import log
from twisted.web import client
from twisted.web.http_headers import Headers
from twisted.web.iweb import IBodyProducer
from twisted.web.server import Site
from twisted.web.static import Data

from buildbot.status.web.base import HtmlResource, path_to_authzfail
from buildbot.status.web.base import path_to_authzfail, path_to_root, path_to_authzfail
