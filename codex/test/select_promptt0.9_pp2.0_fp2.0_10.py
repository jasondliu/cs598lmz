import select
# Test select.select() on a pipe() object.
import os
import select
import time
import unittest
_, w = os.pipe()
to_test = [(select.POLLIN, [r]), (select.POLLOUT, [w])]
if hasattr(select, 'poll'):
    p = select.poll()
    for t, l in to_test:
        p.register(*l, t)

    def run_test(se, t, excepted):
        for fd, ev in se:
            if (ev, fd) not in excepted:
                self.fail('Unexpected result: %s,%s' % (ev, fd))
            excepted.remove((ev, fd))
        if excepted:
            self.fail('Missing result: %s' % repr(excepted))

    def do_poll():
        return p.poll(0.1)


