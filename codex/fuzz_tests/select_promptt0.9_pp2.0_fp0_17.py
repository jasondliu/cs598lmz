import select
# Test select.select and select.poll

import unittest
import os
import errno

from test.support import TESTFN, run_unittest

HOST = 'dummy'
N = 10000


def loop(func, *args):
    i = 0
    while i < N:
        i += 1
        func(*args)


class GeneralTests:

    # No real test here, this is mostly a performance test comparing
    # the two methods

    def _reference(self):
        s = socket.socket(self.family, self.socktype, self.proto)
        s.bind((HOST, 0))
        port = s.getsockname()[1]
        s.listen(5)
        s.setblocking(0)
        i = 0
        while i < N:
            i += 1
            try:
                ns, addr = s.accept()
            except socket.error as e:
                if e.args[0] != errno.EWOULDBLOCK:
                    raise
            else:
                # On success, try to use the socket
