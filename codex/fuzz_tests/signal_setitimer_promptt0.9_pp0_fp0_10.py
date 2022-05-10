import signal
# Test signal.setitimer (alarm) with zosh.
# $Id: signal_setitimer.py,v 1.1 2008/03/23 07:23:27 gram Exp $

print '#',60*'-'
print '# Test signal.alarm (setitimer) with zosh.'
print '#',60*'-'

import os
import sys
sys.stdout.flush()

ticks = os.times()

seconds = 0

alarms = 0

def handler(sig, frame):
    global alarms
    alarms += 1
    #print
    print '!',sig,frame,'!',alarms,'!',seconds
    signal.alarm(1)

signal.alarm(1)
signal.signal(signal.SIGALRM, handler)

for i in range(10):
    signal.pause()

print
print 'seconds elapsed',os.times()[{0:4,1:3,2:2,3:1}[sys.platform[:3]]]-ticks[{0:4,1:3,2
