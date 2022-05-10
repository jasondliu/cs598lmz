import signal
# Test signal.setitimer()
# Test signal.getitimer()
# Test signal.ALARM

import os
import time
import unittest
from test.support import run_unittest, reap_children, get_attribute
from test.support import import_module
thread = import_module('thread')

# Some platforms don't have itimer support.
has_itimer = hasattr(signal, 'setitimer')

# Some platforms don't have SIGALRM, and some have it but not implemented.
alarm_implemented = hasattr(signal, 'SIGALRM')

# Some platforms don't have SIGUSR1.
usr1_implemented = hasattr(signal, 'SIGUSR1')

# Some platforms don't have SIGUSR2.
usr2_implemented = hasattr(signal, 'SIGUSR2')

# Some platforms don't have SIGCHLD.
chld_implemented = hasattr(signal, 'SIGCHLD')

# Some platforms don't have SIGCLD.
cld_implemented = has
