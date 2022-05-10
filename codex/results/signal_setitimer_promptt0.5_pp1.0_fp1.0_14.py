import signal
# Test signal.setitimer()

import os
import time
import signal
import traceback

def handler(signum, frame):
    print 'handler called'
    if signum == signal.SIGALRM:
        print 'handler: SIGALRM'
    elif signum == signal.SIGVTALRM:
        print 'handler: SIGVTALRM'
    else:
        print 'handler: unexpected signal', signum

def main():
    print 'starting'
    signal.signal(signal.SIGALRM, handler)
    signal.signal(signal.SIGVTALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
    for i in range(5):
        try:
            print 'Sleeping'
            time.sleep(0.5)
        except:
            traceback.print_exc()
    print 'done'

main()
