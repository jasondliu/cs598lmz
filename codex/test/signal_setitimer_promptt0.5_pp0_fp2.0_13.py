import signal
# Test signal.setitimer()

import os, sys, time
from test.support import get_attribute, run_unittest, reap_children, \
    unlink

# Skip test if setitimer() is not available
get_attribute(signal, 'setitimer')

# Skip test if alarm() is not available
get_attribute(signal, 'alarm')

# Skip test if SIGALRM is not defined
get_attribute(signal, 'SIGALRM')

# Skip test if SIG_IGN is not defined
get_attribute(signal, 'SIG_IGN')

# Skip test if SIG_DFL is not defined
get_attribute(signal, 'SIG_DFL')

# Skip test if SIGCHLD is not defined
get_attribute(signal, 'SIGCHLD')

# Skip test if ITIMER_REAL is not defined
get_attribute(signal, 'ITIMER_REAL')

# Skip test if ITIMER_VIRTUAL is not defined
get_attribute(signal, 'ITIMER_VIRTUAL')
