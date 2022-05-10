import gc, weakref, os, re
from ws4py.client import connect
from ws4py.client.threadedclient import WebSocketClient
from ws4py.messaging import TextMessage
import json, datetime

from collections import deque, defaultdict
import threading

try:
    from thread import get_ident
except ImportError:
    from threading import get_ident

class BaseHandler(object):
    def __init__(self, *args, **kwargs):
        pass

    def update_state(self, task, state, meta=None):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        pass

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass

class Sender(BaseHandler):
    """
    sender class, sends events through websocket.
    """
    def __init__(self, endpoint, *args
