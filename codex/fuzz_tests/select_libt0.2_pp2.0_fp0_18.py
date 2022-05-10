import select
import socket
import sys
import threading
import time
import traceback

from . import _util
from . import _winapi
from . import constants
from . import events
from . import futures
from . import locks
from . import protocols
from . import transports
from .log import logger
from . import tasks

__all__ = ['BaseEventLoop', 'SelectorEventLoop', 'ProactorEventLoop',
           'new_event_loop', 'get_event_loop', 'set_event_loop',
           'get_child_watcher', 'set_child_watcher']


# A constant that identifies the thread as the main thread.
_PYTHON_MAIN_THREAD_ID = _util.thread_id()


# A constant that identifies the thread as the main thread.
_PYTHON_MAIN_THREAD_ID = _util.thread_id()


# A constant that identifies the thread as the main thread.
_PYTHON_MAIN_THREAD_ID = _util.thread_id()


# A constant that identifies the thread as the
