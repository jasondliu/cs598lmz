import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        signal.signal(signal.SIGALRM, handler)
    else:
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

def run():
    while delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        signal.signal(signal.SIGALRM, handler)
        signal.pause()

if __name__ == '__main__':
    run()
</code>
I want to compute the average execution time for the pseudo-memory and the pseudo-add instructions, calculated from the CPU and/or wall-clock time.
I am trying to use line_profiler to do that.
From the documentation, I read that I am supposed to be able to get a timing for each function by running the following line.
<code>kernprof.py -l -v myscript.py
</code>
However, for me this does not work, as I get a "no such option: -l" error.
<code>usage: kernprof.py [-h] [--line
