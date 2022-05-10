import select
import re
import sys
import os, os.path
import time

from stream import Stream, RE_CHUNK_HEADER
from http import HttpRequest, HttpResponse
from event import Event, EventListener

class HttpProtocol(EventListener):
    """
    HTTP 1.1 Protocol definition. Parses incoming requests and responses
    and passes them to the correct handler
    """
    def __init__(self, sock):
        self.socket = sock
        self.stream = Stream(sock)
        self.parsing_request = False
        self.parsing_response = False
        self.parsing_chunk = False
        self.chunk_size = 0
        EventListener.__init__(self)

    def accept_request(self, request):
        """
        Accept a request. This method should be overridden.
        """
        pass

    def accept_response(self, response):
        """
        Accept a response. This method should be overridden.
        """
        pass
        
