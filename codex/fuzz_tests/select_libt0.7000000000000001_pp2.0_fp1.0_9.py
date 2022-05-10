import select
import socket
import threading
import time
import urllib.request
import urllib.response

from myserver.common.http import http_codes, http_methods
from myserver.common.log import Log
from myserver.common.thread import Thread
from myserver.common.utils import Utils

logger = Log.get_logger(__name__)


class HTTPConnection(object):
    """
    Handles connection to a client.

    POST /test HTTP/1.1
    Host: localhost:8080
    User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.4)
    Gecko/20060508 Firefox/1.5.0.4
    Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
    Accept-Language: en-us,en;q=0.5
    Accept-Enc
