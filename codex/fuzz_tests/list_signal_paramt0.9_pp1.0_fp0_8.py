import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def event_loop():
    while delays:
        time.sleep(max(0, delays.pop(0)))

if __name__ == "__main__":
    if hasattr(signal, "setitimer"):
        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, next(delays))
    else:
        event_loop()
</code>
On my machine the above code with ITIMER_REAL takes around 210 ms to run, while without it takes around 1.2 s.  It also makes a noticeable difference when running meld.

