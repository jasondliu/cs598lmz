import select
# Test select.select() with a large number of file descriptors.

import select
import os

print("start")

# Prepare a large number of file descriptors.

pid = os.fork()
if pid == 0:
    # Child.
    fds = []
    for i in range(10000):
        r, w = os.pipe()
        fds.append(r)
        os.write(w, b"x")
        os.close(w)
    os._exit(0)

# Wait for the child to terminate.
while True:
    try:
        pid, status = os.waitpid(pid, 0)
    except OSError as e:
        if e.errno == errno.EINTR:
            continue
        raise
    break

# Read from all the file descriptors.  This should not crash.
print("select")
r, w, x = select.select(fds, [], [])
print("ok")
