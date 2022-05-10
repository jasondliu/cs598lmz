import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    signal.pause()
</code>
I am getting delays that are too long to be safe:
<code>% python3 timer-test.py
...
0.00011716334095941523
0.0002374988448402127
0.000806900166517501
0.00080192975604479
0.0002934109766502768
0.00042703700006349616
0.000566122667747077
0.0005597472718996955
0.0007592825590862497
0.0004767396748056698
0.0007701277802591
0.0007519050168380861
0.0007691833790983486
...
</code>
The actual code involves a blocking call to <code>read</code> on
