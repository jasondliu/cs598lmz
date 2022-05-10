import select
# Test select.select with a list of sockets, some of which are ssl.SSLSocket,
# and using a timeout of None.
# This test assumes that at least two sockets are readable at once, otherwise
# it hangs.
# The bug was that select.select() returned SSL objects as ints.

import socket
import ssl

# An SSL socket that does *not* block.
class NonBlockingSSL(ssl.SSLSocket):
    def __init__(self, sock, ca_certs):
        ssl.SSLSocket.__init__(self, sock, ca_certs=ca_certs, cert_reqs=ssl.CERT_REQUIRED)
        self.setblocking(0)

    def accept(self):
        try:
            return ssl.SSLSocket.accept(self)
        except ssl.SSLError as e:
            if e.errno == ssl.SSL_ERROR_WANT_READ:
                return (None, None)
            elif e.errno == ssl.SSL_ERROR_WANT_WRITE:
                return
