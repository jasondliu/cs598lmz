import signal
# Test signal.setitimer()
#
# Note that this test can't be run in a subprocess, as the
# signal module checks for the presence of the ITIMER_REAL
# constant (which is not imported into the subprocess's namespace).
print 'Testing signal.setitimer()'

def handler(signum, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.01)
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

print 'Test finished'
