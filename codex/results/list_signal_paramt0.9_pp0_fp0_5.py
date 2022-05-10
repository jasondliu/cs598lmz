import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        raise KeyboardInterrupt

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

for i in range(5*N):
    do_something()
    print(i)
</code>
Running the above code will produce the following output:
<code>...
999
1000
1001
1002
1003
1004
1005
1006
1007
1008

KeyboardInterrupt
</code>
You can add a line <code>print('\n')</code>  in the handler callback to mark where the timer reached the end of your list.

