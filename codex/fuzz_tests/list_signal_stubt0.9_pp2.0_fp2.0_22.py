import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        return

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
while delays:
    gevent.sleep(1)
</code>
Output:
<code>lion@Lion:~/projects/monkey-py2/build$ python script.py 
('!', 69, 0.06589283615903896, 'handler', 'gevent/core.py', 595)
('!', 69, 0.17540894058459994, 'handle_signal', 'gevent/core.py', 1079)
('!', 69, 0.17547702818045994, '__core_signals_unlock', 'gevent/core.py', 1143)
('!', 69, 0.17741484415149992, '__core_signals_lock', 'gevent/core.py', 1157)
('!', 69, 0.17952301022207, 'get_hub', 'ge
