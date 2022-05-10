import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("DONE")
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    time.sleep(.1)
</code>
The code above gives me:
<code>DONE

real    0m4.002s
user    0m0.000s
sys     0m0.000s
</code>
I thought that the <code>time.sleep</code> call would block the execution of the program until the sleep is over.
I thought the program would sleep for at least <code>N * 0.1s</code>, which is <code>1s</code> in this case.
Why is the program not sleeping for 1s?


A:

<code>time.sleep()</code> sleeps for a minimum of the amount of time specified. It doesn't guarantee that it will sleep for that long.
If it did, then we would have a problem: if the program sleeps for a second, then it will sleep for at
