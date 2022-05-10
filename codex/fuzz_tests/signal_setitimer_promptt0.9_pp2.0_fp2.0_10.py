import signal
# Test signal.setitimer() also.
def handler(signum, frame):
    print 'Got signal', signum
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
while True:
    print 'Testing'
    time.sleep(1)

#:TODO:
# Itime extension module
# Threads
# --signal
# PyErr_ExceptionMatches
# test garbage collector
