import signal
# Test signal.setitimer()
#
# This test is Linux-specific.

import os
import signal
import sys
import time
import unittest

from test import support

# Skip test if itimer support is not available.
support.get_attribute(signal, "setitimer")

# Skip test if the required clock is not available.
support.get_attribute(signal, "ITIMER_PROF")

# Skip test if the required signal is not available.
support.get_attribute(signal, "SIGPROF")

# Skip test if the required signal is not available.
support.get_attribute(signal, "SIGALRM")

# Skip test if the required signal is not available.
support.get_attribute(signal, "SIGVTALRM")

# Skip test if the required signal is not available.
support.get_attribute(signal, "SIGCLD")

# Skip test if the required signal is not available.
support.get_attribute(signal, "SIGPOLL")

# Skip test if the required signal is not available.
support
