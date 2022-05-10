import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

min_start = None
max_end = None
last_calls = []

def check(start, end):
    global max_end
    global min_start
    global last_calls
    last_calls.append(end)
    if min_start is None:
        min_start = start
    else:
        min_start = min(min_start, start)
    if max_end is None:
        max_end = end
    else:
        max_end = max(max_end, end)
    while last_calls and last_calls[0] < start - 10e-6:
        last_calls.pop(0)
    if max(start, min_start) - min(end, max_end) > 1e-3:
       
