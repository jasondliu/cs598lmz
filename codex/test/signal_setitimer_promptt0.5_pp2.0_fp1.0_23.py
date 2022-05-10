import signal
# Test signal.setitimer() and signal.getitimer()

# The values of the timer are not very precise.
# On a 2GHz P4, the timer usually expires 50-100ms early.
# On a 266MHz Sparc, the timer usually expires about 2s early.

import sys
import time

