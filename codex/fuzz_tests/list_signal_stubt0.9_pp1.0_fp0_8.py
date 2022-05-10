import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

def on_alarm():
    print("ALARM!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    time.sleep(0.01)
</code>
On my system, both versions use about 10% CPU (as opposed to 2% CPU for the version with <code>sleep()</code>). Nothing wrong with that if it fits your needs, but it might turn out to be too much on old hardware.

