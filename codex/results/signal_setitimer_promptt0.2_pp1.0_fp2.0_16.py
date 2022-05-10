import signal
# Test signal.setitimer()
#
# This test is a bit tricky, because we need to make sure that the
# signal handler is called exactly once.  If we use a simple
# signal.setitimer() call, then the signal handler will be called
# repeatedly, and we can't stop it.  So we use a trick: we set up a
# second timer that will fire after the first one, and then we
# disable the first timer in the signal handler.

def handler(signum, frame):
    print("handler")
    signal.setitimer(signal.ITIMER_REAL, 0)
    signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

while True:
    time.sleep(1)
    print("main")
