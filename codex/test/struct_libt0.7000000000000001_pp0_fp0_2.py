import _struct
import _thread
import _time
import _vars
import _weakref
import _warnings
import errno
import gc
import math
import os
import strop

# Aliases.
import _io
BytesIO = _io.BytesIO
StringIO = _io.StringIO
import _functools
partial = _functools.partial
import _random
random = _random.random
seed = _random.seed
import _socket
from _socket import *
import _ssl
ssl = _ssl
wrap_socket = _ssl.sslwrap
import _thread
start_new_thread = _thread.start_new_thread

import _collections
OrderedDict = _collections.OrderedDict

# CPython's stdlib module, for micropython
# https://github.com/micropython/micropython-lib/tree/master/stdlib

class _NotFound(object):
    pass

_not_found = _NotFound()

