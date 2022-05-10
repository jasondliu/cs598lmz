import select
# Test select.select() using FD 1 as input
fd, filename = tempfile.mkstemp()
try:
    fd = os.fdopen(fd, 'w')
    rfd, wfd, efd = select.select([fd], [], [])
finally:
    os.unlink(filename)

# Test select.select() using FD 1 as output
fd, filename = tempfile.mkstemp()
try:
    fd = os.fdopen(fd, 'r')
    rfd, wfd, efd = select.select([], [fd], [])
finally:
    os.unlink(filename)
