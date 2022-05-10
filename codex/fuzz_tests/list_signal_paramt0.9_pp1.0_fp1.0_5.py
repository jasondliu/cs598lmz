import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, min(delays))

signal.signal(signal.SIGALRM, handler)
# Start the shortest first.
signal.setitimer(signal.ITIMER_REAL, min(delays))
try:
    while delays:
        delays.pop(0)
        print('popped')
except:
    raise
</code>
I was looking into how profilers work and wondered exactly why this little sigalarm-based profiler doesn't work correctly on Windows. I get an occasional RuntimeError: generator ignored GeneratorExit exception from it. After a bit of debugging with print-statements, I traced these exceptions to the following method in <code>threading.py</code>:
<code>def _python_exit():
    for t in enumerate():                        # line 794, Python 3.4.0
        # This time let threads try to kill themselves.
        t._tstate_lock.release()
        try:
            t._stop()
        except AttributeError:   # threading.Thread.__stop is only defined
                                
