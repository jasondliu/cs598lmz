import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2

from debug import *
from lib import *

#------------------------------------------------------------------------------

__all__ = [
    'Client',
    'ClientError',
    'ClientDisconnected',
]

#------------------------------------------------------------------------------

class ClientError(Exception):
    pass

#------------------------------------------------------------------------------

class ClientDisconnected(Exception):
    pass

#------------------------------------------------------------------------------

class Client(object):
    """
    A client is a connection from the user's browser to the server.
    The client keeps track of the current URL, and the currently
    loaded document.
    """
    def __init__(self, server):
        self.server = server
        self.conn = None
        self.addr = None
        self.id = None
        self.url = None
        self.host = None
        self.port = None
        self.path = None
        self.query = None
        self.document_id = None
        self.document = None
        self.redirect_url
