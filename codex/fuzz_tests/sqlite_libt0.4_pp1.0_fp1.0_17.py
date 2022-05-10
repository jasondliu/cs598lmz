import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import platform

# for python2/3 compatibility
if sys.version_info[0] == 3:
    xrange = range

# for python2.6 compatibility
if sys.version_info[:2] < (2, 7):
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

# for python2.6 compatibility
if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# for python2.6 compatibility
if sys.version_info[:2] < (2, 7):
    import unittest2.util as util
    def skipUnless(condition, reason):
        if not condition:
            return lambda obj: None
        return lambda obj: obj
else:
    import unittest.util as util
    from unittest import skipUnless

# for python2.6 compatibility
if sys.version_info[:2] < (2, 7):
    from unittest
