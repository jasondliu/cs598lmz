import signal
# Test signal.setitimer
#
# Run as:
#    python test_signal_setitimer.py

def handler(signum, frame):
    print "got signal", signum

signal.signal(signal.SIGALRM, handler)

def test_setitimer():
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
    #time.sleep(2)

test_setitimer()
