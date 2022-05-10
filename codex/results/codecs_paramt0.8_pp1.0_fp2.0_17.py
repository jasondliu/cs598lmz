import codecs
codecs.register_error("strict", codecs.ignore_errors)

import gzip
import json
import logging
import optparse
import os
import re
import shelve
import sys
import time
from datetime import datetime

from twisted.internet import defer, reactor
from twisted.python import log
from twisted.web import client

from lproxy import common
from lproxy.utils import (
    get_user_agent_string,
    get_http_backend,
    get_http_frontend,
    get_websocket_backend,
)
from lproxy.utils.stacks import (
    domain_stacks,
    domain_image_stacks,
)

from lproxy.network.socket import _open_socket
from lproxy.network.tcp import BaseTCPClient
from lproxy.network.ws.protocol import WebSocketClientFactory
from lproxy.network.http import (
    ProxyClientFactory, HttpClient, ProxyClientFactory, HttpClient,
    HttpRequestLogger,
)


log = logging.getLogger('lproxy')


def
