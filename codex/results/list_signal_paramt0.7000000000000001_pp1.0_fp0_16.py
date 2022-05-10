import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
    
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def exit_handler(signum=None, frame=None):
    signal.setitimer(signal.ITIMER_REAL, 0)
    time.sleep(1)
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)

while True:
    pass
