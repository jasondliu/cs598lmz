import select
# Test select.select().

import select
import socket

def test(args=None):
    if args is None:
        args = []

    if not args:
        args = [0.1]

    timeout = float(args[0])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)

    r,w,e = select.select([s],[],[],timeout)
    if r:
        print "socket should not be ready"
        return 1
    if w:
        print "socket should not be ready"
        return 1
    if e:
        print "socket should not be ready"
        return 1

    s.close()

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(test(sys.argv[1:]))
