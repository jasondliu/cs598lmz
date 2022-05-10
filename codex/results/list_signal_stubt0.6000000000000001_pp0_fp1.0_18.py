import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print(signal.getitimer(signal.ITIMER_REAL))
    else:
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
But, you don't want to use <code>pause</code> in a real program, since it's not portable and it's not interruptible. Instead, you want to use <code>select</code>, <code>poll</code>, or <code>epoll</code> to wait until there's a signal. And you probably want to use <code>SIGEV_THREAD</code> instead of <code>SIGEV_SIGNAL</code> so that you don't have to worry about the signal being delivered in the middle of your code, but that's another question.

