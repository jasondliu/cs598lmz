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
