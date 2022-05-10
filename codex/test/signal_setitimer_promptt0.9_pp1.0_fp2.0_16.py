import signal
# Test signal.setitimer, signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# (0.0, 0.0)
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.0)
signal.getitimer(signal.ITIMER_REAL)
# (1.0, 0.0)
signal.setitimer(signal.ITIMER_REAL, 1.0, 2.0)
signal.getitimer(signal.ITIMER_REAL)
# (1.0, 2.0)
signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
signal.getitimer(signal.ITIMER_REAL)
# (0.0, 2.0)
from contextlib import contextmanager
# Let's work with a tmp file
import tempfile
tmp_file = 'tmp.txt'
with open(tmp_file, 'w') as f:
    f.write('Hello World')
# __
