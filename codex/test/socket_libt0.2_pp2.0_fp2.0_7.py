import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__

try:
    import ssl
except ImportError:
    ssl = None

try:
    import resource
except ImportError:
    resource = None

try:
    import selectors
except ImportError:
    selectors = None

try:
    import asyncio
except ImportError:
    asyncio = None

try:
    import uvloop
except ImportError:
    uvloop = None

try:
    import tornado.platform.asyncio
except ImportError:
    tornado_asyncio = None
else:
    tornado_asyncio = tornado.platform.asyncio.AsyncIOMainLoop()

try:
    import tornado.platform.twisted
except ImportError:
    tornado_twisted = None
else:
    tornado_twisted = tornado.platform.twisted.TwistedIOLoop()

try:
    import twisted
except ImportError:
    twisted = None
