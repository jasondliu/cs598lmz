import io
# Test io.RawIOBase for readability exception handling.

import os
import unittest
import weakref
try:
    import threading
except ImportError:
    threading = None

