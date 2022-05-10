import signal
signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))

if "--psoc5lp" in sys.argv:
    sys.path.append("../../build/cython/psoc5lp")
    import psoc5lp as psoc
elif "--psoc4" in sys.argv:
    sys.path.append("../../build/cython/psoc4")
    import psoc4 as psoc
elif "--stm32f4" in sys.argv:
    sys.path.append("../../build/cython/stm32f4")
    import stm32f4 as psoc
else:
    sys.path.append("../../build/cython/psoc4")
    import psoc4 as psoc

import curses
import math
from collections import OrderedDict
import time
import argparse

class LogDemo(object):
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()
