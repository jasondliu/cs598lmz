import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def issue_sig(n):
    print('Issuing signal')
    os.kill(os.getpid(), signal.SIGALRM)

signal.signal(signal.SIGALRM, handler)

# Trigger the first event after 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Simulate some work after 10 seconds
threading.Timer(10, issue_sig).start()
while delays:
    # GIL will prevent other threads from running
    time.sleep(0.1)
