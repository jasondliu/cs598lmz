import signal
# Test signal.setitimer()

import sys
from test import support

def handler(signum, frame):
    print("Alarm")
    raise SystemExit

@support.require_resource('cpu')
@support.reap_threads
def testit():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
    while True:
        pass

if __name__ == "__main__":
    support.run_unittest(__main__)
