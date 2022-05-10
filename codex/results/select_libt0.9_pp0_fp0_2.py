import select
from errno import EINTR
from threading import Thread
from functools import partial
from StringIO import StringIO
import logging

from HTTPUtils import *

logger = logging.getLogger(__name__)


def errno2exception(f, *arg, **kwargs):
    try:
        return f(*arg, **kwargs)
    except IOError, e:
        if e.errno != EINTR:
            raise
        else:
            return errno2exception(f, *arg, **kwargs)

def handle_request(request_queue, socket, close_event):
    try:
        buf = ''
        while not close_event.is_set():
            try:
                request, args, kwargs = request_queue.get(timeout=1)
                response = request(*args, **kwargs)
            except Queue.Empty:
                if buf:
                    f = partial(socket.send, buf)
                    errno2exception(f)
                    buf = ''
            else:
                if
