import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

if_indextoname = socket.if_indextoname

def test_if_indextoname(index):
    try:
        name = if_indextoname(index)
    except OSError as e:
        if e.errno == errno.EINVAL:
            return None
        raise
    return name

def test_if_indextoname_all():
    for index in range(256):
        name = test_if_indextoname(index)
        if name is not None:
            print('%d: %s' % (index, name))

if __name__ == '__main__':
    test_if_indextoname_all()
