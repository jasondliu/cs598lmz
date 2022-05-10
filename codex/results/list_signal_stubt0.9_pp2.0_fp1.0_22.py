import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

s = socket.socket()
s.bind(('', 52337))
s.listen(5)
while True:
    sock, addr = s.accept()
    sock.send('HTTP/1.1 200 OK\r\n\r\n')
    sock.close()
```

Getting `./slow-replay.py` from a public server with latency more than 70 ms,
we were able to reduce the complexity of WebSocket handshake to O(ms^2) as well:

![](assets/slow-replay.png)

Now it's clear that handshake complexity has nothing to do with having an
encrypted channel to the server. We will only investigate HTTP proxying and
WebSocket proxying further.

## HTTP proxies

### Transparent proxying (regular HTTP)

```python
import socket
import time

sock = socket.socket()
sock.connect(('169.45
