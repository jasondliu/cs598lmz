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
