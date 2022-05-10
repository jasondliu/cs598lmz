import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H')).start()

# Common imports
import numpy as np
import os

# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
