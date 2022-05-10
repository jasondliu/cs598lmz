import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print 'done'
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.pause()
</code>
The real problem is that this code creates a lot of <code>SIGALRM</code> signals, for which the kernel must allocate memory for the signal frames. Sooner or later, this kernel memory will be exhausted and the kernel will start killing processes.
To avoid this problem, you can use a single signal handler per process, and use the <code>sigwait</code> system call to wait for a given signal, instead of using <code>pause</code>. Using <code>sigwait</code> would allow you to avoid the build-up of signal frames, by removing them from the queue as soon as they are handled, so you could sleep for arbitrarily long periods of time. You could also use <code>pselect</code> or <code>ppoll</code> to wait for other events (such
