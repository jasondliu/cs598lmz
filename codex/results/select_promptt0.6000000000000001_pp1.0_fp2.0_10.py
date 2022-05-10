import select
# Test select.select for the following:
# 1. the number of fds that can be monitored at once
# 2. the set of fds that can be monitored at once
# 3. the behavior of select when an fd is closed
#
# Note that this test is run as a subprocess.

import subprocess
import threading
import time
import os

# The maximum number of fds we can select on at once.
MAX_FDS = 1024
# The number of fds we should use for the stress test.
NUM_FDS = 1024

# The command-line arguments we'll use for the stress test.
STRESS_ARGS = {
    'cmd': 'select_stress',
}

# The command-line arguments we'll use for the fd-closing test.
CLOSE_ARGS = {
    'cmd': 'select_close',
}

# The amount of time we'll wait for the stress test to finish.
STRESS_TIMEOUT = 15
# The amount of time we'll wait for the fd-closing test to finish.
CLOSE_TIMEOUT = 30

# The name
