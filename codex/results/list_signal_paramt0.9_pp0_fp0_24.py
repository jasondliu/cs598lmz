import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
The way it works: setitimer is initially configured to issue SIGALRM in a random time. In the handler for SIGALRM, setitimer is called again. If there are no more delays in the list, the handler does nothing. If there are delays left, it sets the next delay. The while loop at the end just pauses until the kernel wakes it up by sending SIGALRM.
Some caveats:

The timings are not really accurate. They are a best-effort approximation. The first delay is processed as accurately as possible, but the subsequent delays can be up to 0.1 sec later than specified. Also, delays that are too close together may be reported by the kernel as "0" and not processed, that's why I added a constant to the delays.
Pauses between SIGALRM's depend on the number of processes and the CPU load. A system under high load may not have time to send even low-priority signals
