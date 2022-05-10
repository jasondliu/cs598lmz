import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
    else:
        print("done")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-3)

for i, d in enumerate(delays):
    if not delays:
        break
    print(d)
    while delays and time.time() - start &lt;= delays[0]:
        pass
    # We're now at delay[0]
    del delays[0]
</code>


A:

The Windows solution, implemented in Python for you, is Waitable Timers.
<code>import ctypes
import time
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

CreateWaitableTimer = ctypes.windll.kernel32.CreateWaitableTimerA
CreateWaitableTimer.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_char_
