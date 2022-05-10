import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)

import sys
def test(sig, frame):
    print("get SIGVTALRM")
    sys.exit(0)

signal.signal(signal.SIGVTALRM, test)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)

while True:
    print("I'm running.")

# Use "ps -eLf | grep timer" to check pid
