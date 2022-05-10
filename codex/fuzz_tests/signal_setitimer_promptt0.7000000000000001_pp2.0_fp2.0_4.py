import signal
# Test signal.setitimer()
# This test is for FreeBSD only, as setitimer() is not available on Linux.
# For other platforms, the test is skipped.

import signal, os, time, errno

def handler(signum, frame):
    print 'handler called for', signum

def setitimer_common(when):
    print when
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
    time.sleep(1)
    # Setting the timer to 0 should disable it
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    time.sleep(1)
    # And the handler shouldn't be called
    print 'done with', when

setitimer_common('main')

# In a subprocess

if os.fork() == 0:
    setitimer_common('subprocess')
    os._exit(0)
else:
    os.wait()

# In a thread

def thread_target():
   
