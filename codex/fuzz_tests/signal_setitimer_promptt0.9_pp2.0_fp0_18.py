import signal
# Test signal.setitimer() and signal.setitimer()
def handler(signum, frame):
    pass

signal.setitimer(signal.ITIMER_REAL, 1, 2)
print 'sleep 5 seconds before catch'
time.sleep(5)
signal.signal(signal.SIGALRM, handler)
# disable SIGALRM, so it will not be catched.
signal.setitimer(signal.ITIMER_REAL, 0, 0) 
time.sleep(10)
print "finish"

# check sys.path and sys.argv
print 'sys.argv[0] is {}'.format(sys.argv[0])
print 'sys.path[0] is {}'.format(sys.path[0])

# check import
import sys
print 'sys.version_info is {}'.format(sys.version_info)
import random
print 'random.randint is {}'.format(random.randint)

# check sys.stdout and sys.stderr
print >> sys.stdout, 'test stdout'

