import signal
# Test signal.setitimer(signame, time) with type time=int

from test import support
import unittest
from test.support import get_attribute, import_module
from test.support import captured_stderr

try:
    raise ImportError
except ImportError:
    signal = import_module('signal')
    getitimer = signal.getitimer
    ITIMER_REAL = get_attribute(signal, 'ITIMER_REAL')
    signal = get_attribute(signal, 'signal')
    pause = signal.pause
    signal = get_attribute(signal, 'signal')
    signal = get_attribute(signal, 'signal')
    signal = get_attribute(signal, 'signal')


# signals
SIGKILL = 9
SIGSCI = 25
SIGCLD = 18
SIGPOLL = 29
SIGSTOP = 19
SIGTSTP = 20
SIGTTIN = 21
SIGTTOU = 22
SIGRTMIN = 34
SIGRTMAX = 64

# quit signal codes
S
