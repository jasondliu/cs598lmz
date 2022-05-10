import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

#---------------------------------------------------------------------

#---------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)

#---------------------------------------------------------------------

import time
for i in xrange(15):
    time.sleep(1)
    print i,

#---------------------------------------------------------------------

import time
for i in xrange(15):
    time.sleep(1)
    print i,

#---------------------------------------------------------------------
