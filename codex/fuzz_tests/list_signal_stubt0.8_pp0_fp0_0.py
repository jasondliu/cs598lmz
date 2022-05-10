import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def sigalrm_handler(signum=None, frame=None):
    print('SIGALRM:', time.time())


signal.signal(signal.SIGALRM, sigalrm_handler)
signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop())
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    signal.pause()
