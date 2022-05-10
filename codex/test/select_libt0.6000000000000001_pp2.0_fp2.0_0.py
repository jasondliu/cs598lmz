import select
import socket
import sys
import time

try:
    import json
except ImportError:
    import simplejson as json

# Python 2.x/3.x compatibility
if sys.version_info[0] < 3:
    import Queue as queue
else:
    import queue

try:
    from urllib.parse import urlparse, urlunparse, urlencode
except ImportError:
    from urlparse import urlparse, urlunparse
    from urllib import urlencode

try:
    import ssl
except ImportError:
    if sys.version_info[0] < 3:
        raise ImportError("Python 2.x without SSL support is not supported")
    else:
        raise ImportError("Python 3.x without SSL support is not supported")

try:
    import websocket
except ImportError:
    raise ImportError("The 'websocket-client' package is required")

__all__ = ['Client', 'Connection']

log = logging.getLogger(__name__)


