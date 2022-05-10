import select
import socket
import sys
import threading
import time

import pytest

from . import test_utils
from .test_utils import (
    assert_logs,
    assert_logs_empty,
    assert_logs_match,
    assert_logs_regex,
)

try:
    import ssl
except ImportError:
    ssl = None

try:
    import http.server as http_server
except ImportError:
    import BaseHTTPServer as http_server

try:
    import socketserver as socketserver
except ImportError:
    import SocketServer as socketserver

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client

try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request

try:
    import urllib.parse as urllib_parse
except ImportError:
    import urlparse as urllib_parse

