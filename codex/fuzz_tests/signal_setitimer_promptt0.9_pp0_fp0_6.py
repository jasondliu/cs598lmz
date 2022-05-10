import signal
# Test signal.setitimer
def handler(a, b):
    raise Exception("got a signal")
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.5)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
# Test setdefaulttimeout
import socket
orig_timeout = socket.getdefaulttimeout()
socket.setdefaulttimeout(0.1)
try:
    time.sleep(0.5)
finally:
    socket.setdefaulttimeout(orig_timeout)
