import gc, weakref
import json
import logging
import os
import re
import sys
import time
import traceback
import types

try:
    import socketio
    import socketio.client
    import socketio.exceptions
except ImportError:
    socketio = None

try:
    import websockets
except ImportError:
    websockets = None

try:
    import aiohttp
except ImportError:
    aiohttp = None

import zmq
from zmq.eventloop import ioloop, zmqstream

import tornado
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, StaticFileHandler
from tornado.websocket import WebSocketHandler

from .display import Display
from . import utils
from . import __version__

if sys.version_info >= (3, 0):
    unicode = str

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Widget classes
# -----------------------------------------------------------------------------

class Widget(object):
    """Base class for all widgets.

    Public attributes:
