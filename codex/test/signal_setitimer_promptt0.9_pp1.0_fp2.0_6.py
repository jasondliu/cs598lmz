import signal
# Test signal.setitimer() on AIX and IRIX.
for sig, args in [
    (signal.ITIMER_REAL, (0.1,)),
    (signal.ITIMER_VIRTUAL, (0.1,)),
    (signal.ITIMER_PROF, (0.1,)),
]:
    it = signal.setitimer(sig, *args)
    if it == (0, 0):
        continue

    raise RuntimeError("setitimer returned %r when setting %r, %r" % (
        it, sig, args
    ))

# Test signal.sigwaitinfo() on IRIX, preliminary:

# Ignore this test in non-multithreaded builds.
if not sys.platform.startswith('irix') or not sys.platform.endswith('6.5') \
or not hasattr(threading, 'Event'):
    raise ImportError('test skipped -- this test must be run on IRIX 6.5')

import threading

all_signals = range(1, signal.NSIG)


