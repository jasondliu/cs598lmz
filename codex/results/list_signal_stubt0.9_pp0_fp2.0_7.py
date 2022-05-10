import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        global total
        print total
        sys.exit()


total = 0
signal.signal(signal.SIGALRM, handler)
handler()
while True:
    total += 1
</code>
It seems that the Python interpreter cannot handle more than 10^7-10^8 interrupts per second. I rounded the loop up to N = 10^8, in which case it took 40-50 seconds before the final time was printed by the script.
In contrast, the equivalent C program (interrupts.c) can give me a total of 10^9 interrupts in around 12 seconds, which is 8x faster.
<code>#include &lt;signal.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/time.h&gt;

void handler(int signum);

int N;
struct timeval delays[1000000];

int main(
