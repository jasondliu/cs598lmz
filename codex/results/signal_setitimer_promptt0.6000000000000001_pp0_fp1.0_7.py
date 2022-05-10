import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

import os
# Test os.pipe
os.pipe()

from subprocess import Popen
# Test os.waitpid
p = Popen(["true"])
os.waitpid(p.pid, 0)

import time
# Test time.sleep
time.sleep(0.1)

import socket
# Test socket.socket
socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import select
# Test select.select
select.select([], [], [], 0.1)

# Test threading
from threading import Thread
t = Thread(target=lambda: None)
t.start()
t.join()

import math
# Test math.exp
math.exp(1)

import cmath
# Test cmath.exp
cmath.exp(1)

# Test ctypes
import ctypes
libm = ctypes.CDLL(None, use_errno=True)
libm.exp.
