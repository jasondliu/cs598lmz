import signal
# Test signal.setitimer()

# This test is not very good.  It doesn't test that the timer actually
# works.  It just tests that the timer can be set and that the signal
# handler is called.

def handler(signum, frame):
    print("handler called")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
