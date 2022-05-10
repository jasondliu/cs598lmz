import mmap
import os
import sys
import tempfile
import time
import traceback
import unittest

from test import support
from test.support import script_helper

# Skip these tests if there is no thread support.
threading = support.import_module('threading')
threading_available = hasattr(threading, 'Thread')

# Skip these tests if there is no threading support.
thread = support.import_module('thread')
threading_available = threading_available and hasattr(thread, 'start_new_thread')

# Skip these tests if the _thread module does not exist.
threading_available = threading_available and hasattr(thread, '_local')

# Skip these tests if the _thread module does not have an allocate_lock function.
threading_available = threading_available and hasattr(thread, 'allocate_lock')

# Skip these tests if the _thread module does not have a get_ident function.
threading_available = threading_available and hasattr(thread, 'get_ident')

# Skip these tests if the _thread
