import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    return

signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
signal.signal(signal.SIGALRM, handler)


import subprocess

def run(i):
    s = time.time()
    p = subprocess.Popen("sleep 0.1", shell=True)
    p.wait()
    print i, time.time() - s

for i in range(N):
    handler()
