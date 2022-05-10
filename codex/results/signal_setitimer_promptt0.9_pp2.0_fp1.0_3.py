import signal
# Test signal.setitimer with SIGPROF profiler
signal.setitimer(signal.ITIMER_PROF, 0.01, 0.02)

import os
import pwd
os.geteuid()
name = pwd.getpwuid(os.geteuid())[0]
print('Hello, ' + name + '!')
