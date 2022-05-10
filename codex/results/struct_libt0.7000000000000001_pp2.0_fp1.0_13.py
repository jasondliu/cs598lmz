import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

from _socket import * # import * is okay in this case
from _weakref import *
from _weakrefset import *

# import the _warnings module in a manner such that warnings are always
# raised, even if python is run with the -O option.
_warnings.catch_warnings()

# These symbols appear in the _thread module but aren't defined
# anywhere else.
error = _thread.error

# The _thread module is too messy to clean up, so just select the
# objects we want from its namespace.  Thread starts automatically.
from _thread import allocate_lock as LockType
from _thread import get_ident as currentThread
from _thread import stack_size
from _thread import start_new as start_new_thread

# Set up the threading exceptions.
error = _thread.error

# Modified version of the original threading.py file by Hye-Shik Chang <perky@FreeBSD.org>
#
