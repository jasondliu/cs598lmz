import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_VIRTUAL, 0)


signal.signal(signal.SIGVTALRM, handler)
handler()

raw_input('press enter')
</code>
When the message is received, the remaining times are stacked on average to N*(2e-04 + 1e-05) time, which will be around 0.15 sec, and the next time will be set to that time.
EDIT: I've found that X does make use of SIGVTALRM for speeding up the cursor blinking and for keeping the keyboard-repeat-rate, so i guess it has its reasons. 

