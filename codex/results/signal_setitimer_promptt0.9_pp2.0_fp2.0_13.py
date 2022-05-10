import signal
# Test signal.setitimer
os.kill(os.getpid(), signal.SIGALRM)
signal.setitimer(signal.ITIMER_REAL, 1)
time.sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0)

import os, sys
print sys.modules["os"].path

# test os.fpathconf
import os
print os.fpathconf(sys.__stdout__.fileno(), 'PC_NAME_MAX')

# testing os.times
import os
t = os.times()
print t
print sum(t)

# testing PIPE
import subprocess, os
c = subprocess.Popen(["echo","hello"], stdout=subprocess.PIPE)
out, err = c.communicate()
print out # "hello\n"
c.wait()

# test cgi
# From: https://code.google.com/p/skulpt/issues/detail?id=90
import cgi
print 'Content-Type: text/html'
print
print '<HTML
