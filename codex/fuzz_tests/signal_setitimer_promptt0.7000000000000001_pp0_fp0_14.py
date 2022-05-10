import signal
# Test signal.setitimer


def handler(signum, frame):
    print('Alarm')
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
#print('\nWaiting...')
#pause()

# This example is a bit dubious, because it assumes that the main
# thread has sole control of the console.  On Linux, this happens to
# be the case, but on other systems, this may be wrong.

# The real-time timer has no effect in this example, because the Python
# interpreter uses an internal 10ms ticker.  The SIGALRM signal is
# queued, but since the handler for that signal is a Python function,
# it is not delivered until the interpreter dispatches the
# signal--which happens only when there is no other Python code to
# execute.  In this case, that happens to coincide with the internal
# 10ms ticker, so the alarm is effectively serv
