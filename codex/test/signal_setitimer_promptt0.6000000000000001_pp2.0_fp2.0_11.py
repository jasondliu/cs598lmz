import signal
# Test signal.setitimer()
#
# Copyright (c) 2003-2004 by Peter Astrand <astrand@lysator.liu.se>
#
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/2.4/license for licensing details.

import unittest
import sys
import time
import os

from test.test_support import run_unittest, reap_children, get_attribute, import_module

thread = import_module('thread')

# On Windows, only SIGBREAK is available.  It acts like SIGINT.
SIGALRM = get_attribute(signal, 'SIGALRM')
SIGBREAK = get_attribute(signal, 'SIGBREAK')
SIGVTALRM = get_attribute(signal, 'SIGVTALRM')
if os.name == 'nt':
    SIGALRM = SIGBREAK
    SIGVTALRM = SIGBREAK

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

