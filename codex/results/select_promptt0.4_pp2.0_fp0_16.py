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

print "Reading...",
sys.stdout.flush()

# This should return immediately.
r, w, x = select.select([r], [], [], 0)

print "OK"

print "Writing...",
sys.stdout.flush()

# This should return immediately.
w, r, x = select.select([], [w], [], 0)

print "OK"

print "Sleeping...",
sys.stdout.flush()

# This should block for a second.
r, w, x = select
