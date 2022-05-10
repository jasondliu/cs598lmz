import signal
# Test signal.setitimer() with a relative expiration (time until SIGALRM)
# The test process should exit before the alarm is delivered.
#
# This test program replaces alarm() in the config.status script of GCC,
# and is used by configure.py

def handler(sig, frame):
    print "got signal", sig
    signal.signal(sig, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
time.sleep(1)
