import signal
# Test signal.setitimer
#
# Signals are:
# ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
#
# See the man page for setitimer for more information.
#
# XXX Problems:
#
# 1. If a signal handler is called while a Python signal handler is executing,
# the Python handler is never called.  We should at least detect this.
#
# 2. Calling signal.setitimer in a signal handler doesn't work as expected
# (documented).  The setitimer call is delayed until the signal handler
# returns.

# Test runner
class TestRunner:
    def __init__(self, test_list):
        self.test_list = test_list
        self.current_test = 0

    def run(self):
        for t in self.test_list:
            self.current_test = t
            t.run()

    def next(self):
        if self.current_test is not None:
            self.current_test.next()

# Test
class Test:
    def __init__(self, name
