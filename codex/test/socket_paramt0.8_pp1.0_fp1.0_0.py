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
