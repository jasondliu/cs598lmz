import signal
# Test signal.setitimer()
#
# Author: Felix Wiemann
# Contact: Felix_Wiemann@ososo.de
# Revision: $Revision: 3259 $
# Date: $Date: 2007-03-09 18:23:28 +0100 (Fri, 09 Mar 2007) $
# Copyright: This module has been placed in the public domain.

"""
Test signal.setitimer().
"""

import unittest
import sys
import os
import signal
import time
import threading

class TestItimer(unittest.TestCase):
    def test_0(self):
        # Need to set the alarm in a different thread, because if the
        # main thread gets interrupted by the timer, the Python code
        # that's supposed to catch it won't be executed.
        def runner():
            signal.setitimer(signal.ITIMER_REAL, 0.01, 0)
            time.sleep(1)
            time.sleep(1)

        thread = threading.Thread(target=runner)
        thread.start()
        thread.join()

