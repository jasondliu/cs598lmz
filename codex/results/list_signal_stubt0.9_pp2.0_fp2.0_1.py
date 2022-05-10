import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        do_something_in_a_long_time()

    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print("Done.")

signal.signal(signal.SIGALRM, handler)

def do_something_in_a_long_time():
    for i in range(1000000):
        pass

handler()
signal.pause()
