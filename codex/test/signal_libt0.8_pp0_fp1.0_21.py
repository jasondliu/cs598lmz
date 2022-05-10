import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time

def test():
    time.sleep(2)
