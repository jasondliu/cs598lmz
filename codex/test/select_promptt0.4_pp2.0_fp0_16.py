import select
# Test select.select() with a non-blocking pipe

# Test select.select() with a non-blocking pipe
#
# This test is not a good idea, because it depends on timing.
# But it's better than nothing.

import select, os, time

r, w = os.pipe()
fl = fcntl.fcntl(r, fcntl.F_GETFL, 0)
fcntl.fcntl(r, fcntl.F_SETFL, fl | os.O_NONBLOCK)

