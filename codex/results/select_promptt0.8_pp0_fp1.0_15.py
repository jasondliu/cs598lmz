import select
# Test select.select()
# By default, select.select() is level triggered
#
# We this following example, we will interface select.select()
# with the blocking pair of r_sock() and w_sock()

import socket

def bind_sock():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    sock.listen(10)
    return sock

def r_sock():
    r, _, _ = select.select([sock], [], [], 1)
    if r:
        return r[0].accept()
    else:
        print('time out')
        return None

def w_sock():
    _, w, _ = select.select([], [sock], [], 1)
    if w:
        return w[0].accept()
    else:
        print('time out')
        return None

# The test suite
if __name__ == "__main__":

    # Create a listening socket
    sock
