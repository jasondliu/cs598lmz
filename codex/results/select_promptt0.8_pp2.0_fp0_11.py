import select
# Test select.select()

from socket import *
import time
import sys

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 0))
s.listen(1)
print 'Listening at', s.getsockname()

def now():
    return time.strftime('%H:%M:%S')

def log(msg):
    print '%s: %s' % (now(), msg)

host, port = s.getsockname()
s2 = socket(AF_INET, SOCK_STREAM)
s2.connect((host, port))

fdmap = {s.fileno(): s, s2.fileno(): s2}

while True:
    log('waiting for connections')
    rs, ws, es = select.select(fdmap, [], [])
    for r in rs:
        if r is s:
            client, addr = s.accept()
            log('client connected from %s:%s' % (addr[0], addr[1]))
            fdmap[client
