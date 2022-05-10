import select
# Test select.select when a file descriptor is set to -1
import os
import sys
import time
from test.support import small_fd_count_warning, reraise_if_not_absolute_path
from test import support
if not hasattr(select, "select"):
    raise support.TestFailed("Test skipped because select.select is not present")
try:
    a, b, c
except NameError:
    stdin, stdout, stderr = 0, 1, 2
cmd = '%s -c "import sys; sys.exit(42)"' % (sys.executable,)
child_args = cmd.split()
child = os.popen(cmd)
try:
    try:
        fd_count = 0
        while select.select([child], [], [], 1.0) == ([], [], []):
            fd_count += 1
            if fd_count > small_fd_count_warning:
                print("warning: test is likely to fail on small FD count systems")
                break
            time.sleep(0.2)
        if 0:
           
