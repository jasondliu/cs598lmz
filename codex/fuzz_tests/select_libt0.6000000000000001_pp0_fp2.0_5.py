import select
import socket
import sys
import threading
import time
import traceback
from collections import deque
from queue import Queue
from threading import Thread
from unittest import mock

from .. import compat
from .. import errors
from .. import events
from .. import futures
from .. import protocols
from .. import transports
from .. import tulip
from ..log import logger
from ..protocol import Protocol
from ..streams import StreamReader
from ..streams import StreamWriter
from .base_events import BaseEventLoopTests
from .base_events import BaseEventLoopTestCase
from .base_events import BaseEventLoopTestCaseMixin
from .base_events import BaseEventLoopMixin
from .base_events import BaseEventLoopMixinTests
from .base_events import _TestSelectorTransport
from .base_events import _TestSocketTransport
from .base_events import _TestWaker
from .base_events import EventLoopTestCase
from .base_events import IsolatedTestCase
from .test_utils import TearDownSelectorMixin
from .test_utils import skipUnless
from
