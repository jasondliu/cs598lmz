import signal
# Test signal.setitimer with max value.
# Super-optimised to prevent setitimer overhead interfering with test timing.
if (not hasattr(signal, "setitimer")) or (not hasattr(signal, "ITIMER_REAL")):
    pass

import time
import signal

def signal_handler(signum, frame):
    print("alarm", time.time() - tt)
    raise Exception("signal_handler")

def main():
    global tt
    signal.signal(signal.SIGALRM, signal_handler)

    # start the timer off as soon as possible..
    signal.setitimer(signal.ITIMER_REAL, 0, 16777216)

    tt = time.time()
    while True:
        pass

main()
