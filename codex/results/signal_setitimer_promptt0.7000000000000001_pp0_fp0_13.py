import signal
# Test signal.setitimer in a subprocess to verify that it can interrupt
# select().

if os.name != 'posix':
    print('Skipping', __file__, 'because not on POSIX')
    exit(0)

import subprocess
import sys


def setitimer_in_subprocess():
    def handler(signum, frame):
        sys.exit(0)
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.2)
    select.select([], [], [])
    sys.exit(1)


child = subprocess.Popen([sys.executable, '-c', setitimer_in_subprocess])
child.wait()
sys.exit(child.returncode)
