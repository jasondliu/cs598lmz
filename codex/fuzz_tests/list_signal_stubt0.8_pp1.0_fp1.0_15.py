import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

    else: 
        print('done')
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
handler()

time.sleep(sorted(delays)[-1])
</code>
But when I run this script, I get an error message:
<blockquote>
<p>Illegal instruction (core dumped)</p>
</blockquote>
Is there something wrong with my code?


A:

Set a timeout for the function using signal module.
<code>import signal

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

# Start the timer. Once 2 seconds are over, a SIGALRM signal is sent.
signal.alarm(2)
</code>
Now invoke the function you want to track.
<code>try:
    decision_maker()   
except
