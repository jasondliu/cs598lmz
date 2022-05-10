import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time

def test():
    time.sleep(2)
    print 34

if __name__ == '__main__':
    test()
