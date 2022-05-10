import signal
# Test signal.setitimer()
# This is only available on Unix.

try:
    signal.setitimer
except AttributeError:
    print("SKIP")
    raise SystemExit

import _thread
import time

def handler(signum, frame):
    print("handler")
    _thread.interrupt_main()

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

try:
    while True:
        print("loop")
        time.sleep(1)
except KeyboardInterrupt:
    print("interrupted")
