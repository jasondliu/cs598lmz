import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
    else:
        global total_value
        print("Total time:", total_value)
        sys.exit(0)

def clock(signum=None, frame=None):
    global total_value
    global start_value
    stop = time.time()
    total_value += (stop - start_value)
    start_value = stop

total_value = 0
start_value = time.time()
signal.signal(signal.SIGALRM, clock)
signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

while True:
    pass
