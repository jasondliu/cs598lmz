import select
import socket
import sys
import threading
import time
import unittest

import eventlet
from eventlet import backoff
from eventlet import debug
from eventlet import event
from eventlet import greenio
from eventlet import hubs
from eventlet import patcher
from eventlet import queue
from eventlet import semaphore
from eventlet import sleep
from eventlet import timeout
from eventlet import util
from eventlet.support import greenlets as greenlet
from tests import LimitedTestCase
from tests import skip_if
from tests import skip_unless
from tests import skip_with_pyevent
from tests.test__socket_dns import setUp, tearDown

eventlet.debug.hub_exceptions(False)

PYPY = hasattr(sys, 'pypy_version_info')

try:
    import ssl
except ImportError:
    ssl = None


