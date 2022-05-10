import select
# Test select.select
timed_out = False
for left in range(4):
    print '  %d seconds left' % (4-left)
    timeout = 4 - left
    r, w, x = select.select([], [], [], timeout)
    if not timed_out and len(r) == 0 and len(w) == 0 and len(x) == 0:
        timed_out = True
        print '  timed out!'
if not timed_out:
    print '  OK!'
import signal

def signal_handler(num, frame):
    print 'Received signal %d in frame %s' % (num, repr(frame))
    signal.signal(signal.SIGWINCH, signal_handler) 
    print 'Caught SIGWINCH, resizing'

signal.signal(signal.SIGHUP, signal_handler)
# Sending an interrupe signal
import os, signal
pid = os.getpid()
print 'my pid is:', pid
print 'Sending myself an interuppt...'
os.kill(pid, signal.S
