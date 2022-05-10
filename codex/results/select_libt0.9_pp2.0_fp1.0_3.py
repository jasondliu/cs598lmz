import select
import errno
import threading
import socket
import logging

from formencode.variabledecode import NestedVariables
from formencode import Invalid, validators

from bpython import __version__
from bpython.repl import Repl
from bpython.config import Struct, loadini, default_config_path
from bpython.curtsiesfrontend import interpreter
from bpython.pager import paginate
from bpython.keys import custom_key_events

struct = Struct()
loadini(struct, default_config_path())

logger = logging.getLogger('bpython')

if 'win' in sys.platform:
    import msvcrt
else:
    import termios
    import fcntl

if 'win' in sys.platform:
    import msvcrt
    class Event:
        def __init__(self):
            self._bool = False
        def wait(self, timeout=None):
            return self._bool
        def set(self):
            self._bool = True
        def clear(self):
            self._bool
