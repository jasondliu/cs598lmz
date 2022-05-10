import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    elif signal.getitimer(signal.ITIMER_REAL)[0] is not 0.0:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# python timer.py
# PID: 5802
# PPID: 5801
# UID: 501
# EUID: 501
# GID: 20
# EGID: 20

# $ pstree -s 5801
# bash(5801)─┬─bash(5801)─┬─docker(5802)
#           │             ├─ssh(5803)───bash(5804)─┬─python(5807)───{python}(5818)
#           │             │                          ├─{python}(5808)─┬─{python}(5819)
#           │             │                          │                 └─{python}(5821)
#          
