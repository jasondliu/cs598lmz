import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

import logging
# logging.basicConfig(level=logging.DEBUG)

import os
import sys
import time
import zmq

from functools import partial
from itertools import count
from threading import Thread

from . import config
from . import utils

log = logging.getLogger(__name__)


class Broker(object):
    """
    Broker is a ZeroMQ proxy that routes messages between publishers and
    subscribers.

    """

    def __init__(self, frontend_addr, backend_addr,
                 frontend_bind=True, backend_bind=True,
                 context=None,
                 frontend_hwm=None, backend_hwm=None,
                 frontend_swap=None, backend_swap=None,
                 frontend_affinity=None, backend_affinity=None,
                 frontend_identity=None, backend_identity=None,
                 frontend_sndhwm=None, backend_sndhwm=None,
                
