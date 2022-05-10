import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_REAL, 0)
signal.signal(signal.SIGALRM, handler)
handler()

for i in range(3):
    time.sleep(0.5)
</code>
The script generates <code>N</code> random delays and sends <code>SIGALRM</code> signals after each of them. To emulate <code>SIGINT</code>s, I've created <code>SIGINT</code> signal handler in the main thread.
<code>import signal
import threading

def handler(signum=None, frame=None):
    print('SIGINT')

t = threading.Thread(target=time.sleep, args=(3600,))
t.daemon = True
t.start()
signal.signal(signal.SIGINT, handler)
t.join()
</
