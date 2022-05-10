import select
import logging
import sys

from io import BytesIO   # Python 3

from webbrowser import open as open_in_browser

from ..utils import ask, _close_on_exec, select_port
from ..utils import safe_join, getcwd, getmtime, wait_for_file
from ..contrib.grid_arrow import GridArrow
from .dtables import DumbTable
from .progress import Progress
from .form_parser import parse_form_data
from .exceptions import AbortRequest
from .security import generate_safe_token
from .http_protocol import parse_http_headers, HTTPConnection, HttpError

try:    # Python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, unquote, urlsplit, urljoin, quote
except ImportError:  # Python 2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    from urlparse import parse_qs, unquote, urlsplit, urljoin
    from urllib import quote

if imp.PY
