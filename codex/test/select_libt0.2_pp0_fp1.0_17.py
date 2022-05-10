import select
import socket
import sys
import time
import traceback

import pytest

from . import util

try:
    import ssl
except ImportError:
    ssl = None

try:
    import OpenSSL
except ImportError:
    OpenSSL = None

try:
    import cryptography
except ImportError:
    cryptography = None

try:
    import idna
except ImportError:
    idna = None

try:
    import certifi
except ImportError:
    certifi = None

try:
    import urllib3
except ImportError:
    urllib3 = None

try:
    import requests
except ImportError:
    requests = None

try:
    import urllib.request
except ImportError:
    urllib_request = None
else:
    urllib_request = sys.modules["urllib.request"]

try:
    import http.client
except ImportError:
    http_client = None
