import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('All timers done.')
        raise Exception

# Schedule the first event.
signal.signal(signal.SIGALRM, handler)
handler()

# Loop until all timers have fired (will get an exception from
# handler).
while True:
    try:
        # This is a blocking call, so we'll eventually get
        # an exception when all timers are done.
        signal.pause()
    except:
        break
