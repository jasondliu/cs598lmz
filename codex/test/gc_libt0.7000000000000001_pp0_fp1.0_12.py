import gc, weakref

import _thread
import threading
import _testcapi
import time
import os
import sys
import unittest
import subprocess
import warnings

# We need to have a threading.Thread object in order to test
# _thread._count(), so just create a dummy one.
THREAD_DUMMY = threading.Thread()

# Don't use support.threading_setup() since _thread isn't
# an implicit import.
import _thread
