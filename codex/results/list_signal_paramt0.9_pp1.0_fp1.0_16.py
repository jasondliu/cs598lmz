import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        print('{}'.format(N - len(delays)))
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
while True:
    pass
</code>
As you can see, this program is pretty simple.  It just counts from 1 to 10000 and sleeps for a random amount of sleep specified in the <code>delays</code> list.  The problem is, when I timeout waiting for an http response after <code>timeout=1</code>.  My program hangs and will not continue.  The timeout code I am using is as follows:
<code>file = urllib.request.urlopen(request, timeout=1)
</code>
I don't understand why a timeout would cause my program to hang...

