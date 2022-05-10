import select
# Test select.select() is implemented.
import select
# Test socket.socketpair() is implemented.
import socket
try:
    socket.socketpair()
except:
    print("SKIP")
    raise SystemExit

# Test signal.setitimer() is implemented.
import signal
signal.setitimer(signal.ITIMER_REAL, 0, 1000)

# Test time.sleep() is implemented.
import time
time.sleep(0.1)

# Test uerrno is implemented.
import uerrno
uerrno.EINVAL

# Test uheapq is implemented.
import uheapq
uheapq.heappush(list(), 'a')
uheapq.heappop(list())

# Test uhashlib is implemented.
import uhashlib
uhashlib.sha256(b"hello").digest()

# Test uio is implemented.
import uio
uio.StringIO('hello')

# Test ujson is implemented.
import ujson
ujson.dumps([1, 2])

# Test u
