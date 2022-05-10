import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.stdout.write('\n')
        sys.exit(0)

for SIG in (signal.SIGALRM, signal.SIGIO, signal.SIGPOLL, signal.SIGPROF):
    try:
        signal.signal(SIG, handler)
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        break
    except ValueError:
        pass
else:
    sys.stdout.write('\n')
    sys.exit(0)
</code>
In cygwin, this will never poll.
<code>// poll.c //

#include &lt;poll.h&gt;
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/time.h&gt;
#include &lt;sys/signal.h&gt;

#define N 1000

struct pollfd pfd
