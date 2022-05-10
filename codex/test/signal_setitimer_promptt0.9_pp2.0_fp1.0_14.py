import signal
# Test signal.setitimer
# NOTE: this will cause our script to receive a SIGVTALRM after 1 second
signal.setitimer(signal.ITIMER_VIRTUAL, 1.0)
# This will block, as per usual. Since we're blocking on the main thread, there
# are many things that would cause problems (KeyboardInterrupt, etc.). A common
# solution is to use a separate thread to block, e.g. using signals.sigwaitinfo
signal.sigwaitinfo({signal.SIGVTALRM})

import contextlib
# Show how context managers work with __exit__()
# Note: the object that actually matters is the value returned by __enter__(),
# since it is stored and accessible from the as-variable inside the with block
@contextlib.contextmanager
def test():
    print('Starting')
    yield
    print('Exiting')

with test() as t:
    print('Doing something...')

@contextlib.contextmanager
def testarg(arg):
    print('Starting')
    yield arg
    print('Exiting')

