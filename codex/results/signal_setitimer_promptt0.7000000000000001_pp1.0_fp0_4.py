import signal
# Test signal.setitimer()

interval = 1.0

def handler(signum, frame):
    print("signal", signum, "at", time.ctime())

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, interval, interval)
while True:
    time.sleep(3)
 
import signal
# Test signal.setitimer()

interval = 1.0

def handler(signum, frame):
    print("signal", signum, "at", time.ctime())

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, interval, interval)
while True:
    time.sleep(3)
 
import signal
# Test signal.setitimer()

interval = 1.0

def handler(signum, frame):
    print("signal", signum, "at", time.ctime())

signal.signal(signal.
