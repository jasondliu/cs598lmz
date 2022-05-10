import select
# Test select.select() interface
select.select([], [], [], 0.0)

# Test the poll() interface
try:
    import select
except ImportError:
    raise ImportError("skipping poll test, select module not available")

p = select.poll()

import os
import errno

try:
    fd = os.open('/dev/null', os.O_RDONLY)
except OSError:
    raise ImportError("skipping poll test, /dev/null not available")

# Make sure the file descriptor is closed when the test is over,
# and make sure the test doesn't crash when p.poll() is called
# after p.unregister().
p.register(fd, select.POLLIN)
p.unregister(fd)
os.close(fd)

# Test select.poll() on an empty poll object.
import time

# Wait up to 10 seconds for an event.
for timeout in [0, 10]:
    start = time.time()
    r = p.poll(timeout)
    elapsed = time.time() - start

