import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)
</code>
A value such as 0.00000105 that is more than 1e-6 but less than 3e-6 will take 0.000001xx, 1e-6 takes 0.000001xx, and 2e-6 takes 0.000002xx. A value such as 0.000002xx will take the same 0.000002xx, and the next 0.000002xx will take 0.000002xx and 0.000003xx, by which time a value such as 0.00000109 that is more than 1e-6 but less than 3e-6 will take 0.00000109, 1e-6 will take 0.00000109, and 2e-6 will take 0.00000209.
With a loop using <code>time.sleep()</code>, a value such as 0.00000104 that is more than 1e-6 but less than 3e-6 will take 1e-6, and 1e-6 will take 1e
