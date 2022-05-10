import signal
# Test signal.setitimer and signal.alarm

import os
import sys
from test import support
import signal
import subprocess
import time
import unittest

from test.support import reap_children, get_attribute
from test.support.script_helper import assert_python_ok

class AlarmException(Exception):
    pass

def alarm_received(n, frame):
    raise AlarmException

