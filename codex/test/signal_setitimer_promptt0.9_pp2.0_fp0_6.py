import signal
# Test signal.setitimer, signal.getitimer, signal.setitimer, signal.getsignal,
# signal.default_int_handler to make sure they work as expected.

signum = signal.SIGABRT

signal.getsignal(signal.SIGABRT) == signal.default_int_handler
signal.default_int_handler(signum, None)

# register 'foo' as a signal handler for SIGALRM
def foo(a, b):  foo.hits += 1
foo
