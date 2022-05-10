import signal
# Test signal.setitimer, signal.getitimer and signal.ITIMER_REAL
import signal, os, sys, time

def signal_handler(signum, frame):
    print("Received signal", signum)
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, signal_handler)

# 0.5 second
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

try:
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("")
    print("OK")
