import signal
# Test signal.setitimer()
import time

def handler(signum, frame):
    print("got alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
print("waiting...")
time.sleep(2)
print("done")

# Test signal.getsignal()
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)
print(signal.getsignal(signal.SIGINT))

signal.signal(signal.SIGINT, signal.SIG_DFL)
print(signal.getsignal(signal.SIGINT))

# Test signal.pause()
import signal
import time

def handler(signum, frame):
    print("got alarm")
    signal.alarm(1)

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)
signal.pause()

# Test signal.set
