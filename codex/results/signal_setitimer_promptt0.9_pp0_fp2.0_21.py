import signal
# Test signal.setitimer()
import select
import socket

class SigAlarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise SigAlarm

signal.signal(signal.SIGALRM, alarm_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("python.org", 80))
signal.setitimer(signal.ITIMER_REAL, 0.1)
try:
    while 1:
        # Wait for 10 seconds for an event
        r, w, e = select.select([s], [], [], 10)
        if s in r:
            # We got an event; read some data
            data = s.recv(4096)
            print data
            # There's no more data
            break
        # Select again
    else:
        print "No data within 10 seconds"
except SigAlarm:
    print "Got SIGALRM"
# We're done; disable the alarm
signal.setitimer(signal.ITIMER_RE
