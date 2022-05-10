import signal
# Test signal.setitimer and signal.setitimer.
# This is a test for SF bug #1046288.
#
# Without any changes, this script causes Python to crash with a "Segmentation
# fault" on Linux/x86.

import time
#import signal

