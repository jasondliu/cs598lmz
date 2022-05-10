import socket
import sys
import re
import os
import time
import threading
import signal
import select
import errno
import logging
import logging.handlers
import traceback
import datetime

#
# Global variables
#

# The server's hostname
HOST = 'localhost'

# The server's port
PORT = 8080

# The socket used to communicate with the server
server_socket = None

#
# Functions
#

# This function takes a string containing an HTTP request and parses it into
# three parts: the request line, headers, and body
def parse_http_request(request):
    # First, we split the request by the double CRLF that separates the
    # headers from the body
    request_parts = request.split('\r\n\r\n', 1)
    headers = request_parts[0]
    body = ''
    if len(request_parts) == 2:
        body = request_parts[1]

    # Next, we split the headers by CRLF to get a list of header lines
    header_lines = headers.
