import select
# Test select.select().

import sys
import time
import select

if sys.version_info[:2] == (2, 6):
    # Python 2.6 added a timeout parameter to select.select.
    TIMEOUT_SUPPORT = True
else:
    TIMEOUT_SUPPORT = False

def test_select():
    fd = sys.stdout.fileno()

