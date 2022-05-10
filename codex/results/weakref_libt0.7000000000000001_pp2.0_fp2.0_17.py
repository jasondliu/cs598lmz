import weakref
import time
import datetime
import functools
import collections

from . import exc
from . import utils
from . import logging
from . import events
from . import compat
from . import api
from . import protocols
from . import futures
from . import tasks
from . import schedules
from . import states


class Task(futures.Future):
    """Base class for all task implementations."""

    __slots__ = (
        '_logger', '_repr_info', '__weakref__', 'app',
        'name', 'id', 'uuid', 'args', 'kwargs',
        '_state', '_task_id', '_retries', '_eta',
        '_expires', '_result', '_exception', '_tb', '_callbacks',
        '_errbacks', '_on_ack', '_on_reject', '_on_accept',
        '_on_revoke', '_on_retry', '_receiver', '_priority',
        '_request_dict', '_accepted',
