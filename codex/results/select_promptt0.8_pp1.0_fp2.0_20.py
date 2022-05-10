import select
# Test select.select, and select.unselect
# with datagram protocol

import socket
import time

# create datagram sockets

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def check(msg, s1, s2):
    print msg
    r, w, e = select.select([s1], [s2], [], 1)
    print r, w, e

check('no data', s1, s2)
s1.sendto('xxx', ('127.0.0.1', 0))
s1.sendto('xxx', ('127.0.0.1', 0))
s2.sendto('xxx', ('127.0.0.1', 0))
s2.sendto('xxx', ('127.0.0.1', 0))
check('before select', s1, s2)
select.select([s1], [], [], 1)
check('after recv data s1', s1,
