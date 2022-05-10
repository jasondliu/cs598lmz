import select
# Test select.select() for a timeout value of 0.0

# This test is not very robust.
# It can fail when the system is loaded.

import errno

readable, writable, exceptional = select.select([], [], [], 0.0)

if readable != [] or writable != [] or exceptional != []:
    raise RuntimeError("select() returned %s %s %s" % (readable, writable, exceptional))

readable, writable, exceptional = select.select([], [], [], 0)

if readable != [] or writable != [] or exceptional != []:
    raise RuntimeError("select() returned %s %s %s" % (readable, writable, exceptional))

try:
    select.select([], [], [], 0.1)
except select.error as e:
    if e.args[0] != errno.EINTR:
        raise RuntimeError("select() raised %s not EINTR" % e)
else:
    raise RuntimeError("select() did not raise an exception")
