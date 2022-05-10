import threading
threading.Thread.daemon = True
import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.escape import to_unicode, json_encode, json_decode
from tornado.gen import coroutine
import signal
import asyncio
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass
from threading import Event
import json
import uuid
from io import BytesIO
import base64
from six.moves import html_parser
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.simple_httpclient import SimpleAsyncHTTPClient
import tornado.platform.asyncio
from async_timeout import timeout
from . import logger


class WebSocketRequestHandler(WebSocketHandler):
    def initialize(self, on_open=None, on_message=None, on_close=None, on_error=None):
        self.on_open = on_open

