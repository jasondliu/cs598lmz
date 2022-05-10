import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())


def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0, 1e-6)
    while delays:
        pass

main()
</code>
Results:
<code>$ python3 test.py
Wall time: 30.95 s
$ python3 test.py
Wall time: 30.94 s
$ python3 test.py
Wall time: 30.37 s
</code>

Using Python 3.7.2 / Linux x86_64, i7 CPU, SSD, Python built with GCC x86_64-linux-gnu-gcc (Debian 8.3.0-4) 8.3.0

