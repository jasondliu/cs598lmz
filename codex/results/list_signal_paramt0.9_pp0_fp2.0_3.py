import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def setup_signal_handler():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def main():
    setup_signal_handler()
    while delays:
        pass

main()
</code>


A:

You want to use signal.setitimer. You can pass a 2-tuple with the seconds and microseconds as the first argument:
<code>&gt;&gt;&gt; import signal
&gt;&gt;&gt; signal.setitimer(signal.ITIMER_REAL, 0.01)
</code>
After the specified time you will get a signal.
You can also pass a 3-tuple with the seconds, microseconds, and the time that should elapse before the signal to send before the signal will start to be sent periodically. In your case, that would be:
<code>signal.setitimer(signal.ITIM
