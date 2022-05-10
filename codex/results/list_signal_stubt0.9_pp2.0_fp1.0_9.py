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
handler()

while delays: time.sleep(1e9)
print("finito!")
</code>
I have encountered a problem on a <code>numpy</code> script where I import this module and the <code>SIGALRM</code> signal was intercepted.
I managed to solve this problem in a pretty ugly way by appending <code>signal.signal(signal.SIGALRM, signal.SIG_DFL)</code> after the last import statement (where I know I'm done importing stuff).
The question: what are the implications of trapping <code>SIGALRM</code>?

