import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc\n')).start()
import time
time.sleep(3)

'''

from __future__ import print_function
import os
import sys
import time
import threading
print('%s: starting' % os.getpid(), file=sys.stderr)


def child():
    print('%s: child started' % os.getpid(), file=sys.stderr)
    sys.stdout.write('Client started\n')
    while True:
        pass
    print('Client ended\n')
    print('%s: child ended' % os.getpid(), file=sys.stderr)
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('%s: parent ended' % 'Parent', file=sys.stderr)
            time.sleep(1)  # sleep 1 sec so child can print
        # this is parent; loop to create next child


parent()
