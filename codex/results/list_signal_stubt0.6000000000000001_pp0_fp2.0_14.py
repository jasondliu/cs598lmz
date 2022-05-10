import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print(signum, frame)
        print(signal.__dict__)
        print(signal.SIG_DFL)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        sys.exit(0)


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while 1:
    time.sleep(1)
</code>
The output looks like:
<code>14 &lt;frame object at 0x7fbbf2e0cdb0&gt;
{'SIG_DFL': 0, 'SIG_IGN': 1, 'NSIG': 32, 'SIGABRT': 6, 'SIGALRM': 14, 'SIGBUS': 7, 'SIGCHLD': 17, 'SIGCLD': 17, 'SIGCONT': 18, 'SIGFPE': 8, 'SIGHUP': 1, 'SIGILL': 4, 'SIGINT': 2, '
