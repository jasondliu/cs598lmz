import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)


class TimeoutError(Exception):
    pass


def timeout(signum=None, frame=None):
    raise TimeoutError()


def run():
    global delays
    signal.signal(signal.SIGALRM, timeout)
    signal.signal(signal.SIGVTALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
    time.sleep(100)
    
run()
