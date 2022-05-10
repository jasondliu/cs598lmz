import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

def handler(signum, frame):
   print ("Forever")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
   pass
