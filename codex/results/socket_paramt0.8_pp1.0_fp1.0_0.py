import socket
socket.if_indextoname(2)

# <codecell>

import rpyc
from rpyc.utils.zerodeploy import DeployedServer

# <codecell>

server = DeployedServer("bla")
server.start()
server.accept()

# <codecell>

server.stop()

# <codecell>

import time
ct = time.time()
server.wait()
print time.time() - ct

# <codecell>

server._stop_event.is_set()

# <codecell>

import socket
import sys
import rpyc
conn = rpyc.classic.connect("localhost")

# <codecell>

def f():
    for i in range(10):
        yield i

# <codecell>

f()

# <codecell>

f().next()

# <codecell>

a = "123"
a.__next__()

# <codecell>

class A(object):
    def __next__(self):
        return 1
    def __
