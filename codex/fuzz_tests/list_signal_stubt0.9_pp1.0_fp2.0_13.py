import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def late_call():
    for i, delay in enumerate(delays):
        signal.setitimer(signal.ITIMER_REAL, delay)
        signal.signal(signal.SIGALRM, handler)
        while delays:
            time.sleep(1)
    print("All callbacks finished")

late_call()
</code>

