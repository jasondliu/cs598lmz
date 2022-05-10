import signal
# Test signal.setitimer()
#
# Note that this program is not intended to be run directly.  It is
# run by the test-itimer.sh script.

def handler(signum, frame):
    print("handler")
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    print(".")
    time.sleep(1)
