import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays[0], 0)
        delays.pop(0)
        print('Signalled: {}'.format(signum))

signal.signal(signal.SIGALRM, handler)
with open('/tmp/out.txt', 'w') as stdout:
    sys.stdout = stdout
    med = sorted(delays)[N // 2 - 1]
    signal.setitimer(signal.ITIMER_REAL, med, 0)
    input()
</code>
Here's a Linux-based way for a general case (with the necessary inspiration coming from this answer):
<code>import subprocess
import re

def sync_per():
    res = subprocess.check_output('ps -ef | grep "python" | grep -v "grep"', shell=True)
    res = res.decode('utf-8').split('\n')[:-1]
    return sorted(int(re.match(r'\w+\s+(\d+)\s+\d+:\d+:\d+.
