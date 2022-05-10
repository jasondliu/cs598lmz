import select
import socket
import sys
import threading
import time
import traceback

import numpy as np

from . import common
from . import events
from . import geometry
from . import glfw
from . import keycodes
from . import platform
from . import window
from . import window_impl
from . import window_impl_glfw
from . import window_impl_x11


#: The number of seconds between calls to :meth:`events.EventDispatcher.process_events`
#: from the main thread.
EVENT_DISPATCH_PERIOD = 1.0 / 60.0

#: The number of seconds between calls to :meth:`window.Window.swap_buffers`
#: from the main thread.
SWAP_BUFFERS_PERIOD = 1.0 / 60.0

#: The number of seconds between calls to :meth:`window.Window.invalidate`
#: from the main thread.
INVALIDATE_PERIOD = 1.0 / 10.0

#: The number of seconds between
