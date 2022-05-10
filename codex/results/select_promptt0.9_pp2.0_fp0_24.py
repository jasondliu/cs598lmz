import select
# Test select.select.

import select, errno
from test.support import TESTFN, findfile, unlink

# These tests assume that select.select is implemented
# with the underlying system call rather than a simulation (Python implementation).
# This requires a select implementation which is interruptible
# with a signal and the signal implementation has to be sane (see the docs).

class InterruptedSocket:

    def __init__(self, sock=None):
        if sock is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', 0))
            sock.listen(1)

        self.sock = sock
        self.interrupted = False

    def accept(self):
        (clientsocket, address) = self.sock.accept()
        return (clientsocket, address)

    def close(self):
        self.sock.close()
        # The stack involving socketmodule.c will be cleaned on the next
        # call to space_newdict().
        support.gc_collect()

    def __getattr__(self
