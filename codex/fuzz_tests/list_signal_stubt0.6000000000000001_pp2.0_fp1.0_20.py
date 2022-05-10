import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

print("Starting")
while delays:
    signal.pause()
print("Ending")
</code>
This is a little more complicated than the first example, but it also demonstrates the power of the signal API.  The <code>signal.ITIMER_REAL</code> timer is a real-time timer, and the <code>signal.setitimer()</code> function sets the timer to the specified number of seconds.  The <code>signal.pause()</code> function waits until a signal is received, and the <code>signal.signal()</code> function hooks the handler function to the <code>SIGALRM</code> signal, which is the signal that is sent when the timer expires.

