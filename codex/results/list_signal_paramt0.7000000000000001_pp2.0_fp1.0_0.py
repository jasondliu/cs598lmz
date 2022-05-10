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
signal.setitimer(signal.ITIMER_REAL, delays[-1])

while delays:
    time.sleep(2)
    print(time.time())
print(time.time())
</code>
Output:
<code>1520284898.8867672
1520284898.8877673
1520284898.8887674
1520284898.8897676
1520284900.8578088
1520284900.8588103
1520284900.859811
1520284900.860812
1520284902.8288147
1520284902.8298153
1520284902.830816
1520284902.8318166
1520284904.7988206
1520284904.
