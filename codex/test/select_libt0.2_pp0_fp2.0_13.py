import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

from . import util
from . import version

__all__ = ['ProxyHandler', 'ProxyHandlerChain', 'ProxyError', 'Proxy',
           'ProxyRequest', 'ProxyResponse', 'ProxyConnection',
           'ProxyServer']

class ProxyHandler(object):
    """
    Base class for proxy handlers.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, req, resp):
        """
        Handle the given request and response.
        """
        if self.next_handler:
            self.next_handler.handle(req, resp)

