import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        f = open('/tmp/out.txt', 'w')
        f.write('done')
        f.close()
        sys.exit(0)

handler()
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while True:
    pass
</code>
The code above will generate a sequence of delays and write <code>done</code> to a file when all the delays have executed (and exit).
When I run this code in the Python interpreter with <code>python -i test.py</code>, it works flawlessly. However, when I run it as a script with <code>python test.py</code>, the <code>done</code> file is never written.
Why does it behave differently depending on whether it's run in the interpreter or as a script?


A:

On Unix systems, the <code>SIGALRM</code> signal is ignored by default in
