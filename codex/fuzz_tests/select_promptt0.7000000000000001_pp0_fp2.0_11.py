import select
# Test select.select()

# select.select([rlist],[wlist],[xlist], [timeout])
# - rlist: waiting for read
# - wlist: waiting for write
# - xlist: waiting for exception
# - timeout: waiting time, wait forever if timeout is None, return immediately if timeout is 0

# select.select() return (rlist, wlist, xlist)

# rlist, wlist, xlist are tuple
# - rlist: readable
# - wlist: writable
# - xlist: errorable
# rlist, wlist, xlist are empty if timeout

def test_select():
    import socket
    import random
    import time
    from common import *
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = random.randint(8000, 9000)
    s.bind((host, port))
    s.listen(1)
    print('listen on %s:%d' % (host, port))
    client, addr = s
