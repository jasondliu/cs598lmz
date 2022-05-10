import signal
# Test signal.setitimer, signal.getitimer, signal.ITIMER_REAL and
# signal.ITIMER_VIRTUAL.

# This test is based on the itimer.c test from the GNU C library.

import sys
import time
import unittest
from test import support

def handler(signum, frame):
    pass

class ItimerTest(unittest.TestCase):
    def test_itimer(self):
        # The test is based on the itimer.c test from the GNU C library.
        # Copyright (C) 2002-2016 Free Software Foundation, Inc.
        # This program is free software: you can redistribute it and/or modify
        # it under the terms of the GNU General Public License as published by
        # the Free Software Foundation; either version 3 of the License, or
        # (at your option) any later version.
        #
        # This program is distributed in the hope that it will be useful,
        # but WITHOUT ANY WARRANTY; without even the implied warranty of
        # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
