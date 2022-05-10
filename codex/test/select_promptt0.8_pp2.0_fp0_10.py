import select
# Test select.select()'s ability to list open files using the non-blocking
# descriptor.  See
#    http://bugs.python.org/issue3510
#    http://bugs.python.org/issue2713
# This test program should finish in under 30 seconds.  On Windows, it
# typically finishes in less than 2 seconds.
#
# This test program must be run with the -u command line argument;
# otherwise, we won't get a full traceback for a failed test.

import os
import select
import signal
import sys
import threading
import time

def fatal(msg):
    print(msg)
    print("FAIL")
    sys.exit(1)

print("Testing select.select() with a large number of pipes.", flush=True)
print("This test may take 30 seconds on Windows.", flush=True)

program = sys.argv[0]
if sys.executable:
    program = sys.executable

# This test program must be run with the -u command line option.
