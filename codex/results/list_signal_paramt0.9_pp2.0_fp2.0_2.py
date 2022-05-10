import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print(time.clock())

signal.setitimer(signal.ITIMER_REAL, delay=0)
signal.signal(signal.SIGALRM, handler)
</code>
I have some problems with this code, it doesn't work like timer and keep program stuck. If it's possible I would prefer to use only one timer but I accept solution with as many timers as points of time.


A:

It looks like <code>signal.setitimer()</code> isn't the right tool for what you want. The Python docs state that it can't be called in a signal handler:
<blockquote>
<p>Please note, however, that the POSIX setitimer() and Windows SetTimer() feature allows repeated timer expirations, potentially at very high rates. <strong>On some systems, however, the underlying setitimer() or SetTimer() will not actually cause more than one signal to be queued</strong>. If the signal handler calls setitimer() or SetTimer() requesting a repetition rate higher than the underlying system
