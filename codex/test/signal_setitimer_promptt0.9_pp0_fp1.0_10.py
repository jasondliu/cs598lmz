import signal
# Test signal.setitimer(signal.ITIMER_PROF, 1.0)
"""
import signal
signal.signal(signal.SIGPROF, lambda signum, frame: sys.stdout.write('\n'))
signal.setitimer(signal.ITIMER_PROF, 1.0)  # 1 second interval
"""

import sys
def test():
    fs = []
    for i in range(10000):
        fs.append(sys._current_frames())
    return len(set([ id for f in fs for id in f.values() ]))

print(test())
