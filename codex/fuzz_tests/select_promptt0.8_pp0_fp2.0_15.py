import select
# Test select.select() behavior regarding a write-only file descriptor.
fds = []
stdin = sys.stdin.fileno()
fds.append(stdin)
fds.append(sys.stdout.fileno())
fds.append(sys.stderr.fileno())
fds.append(100)
print fds
try:
    rfds, wfds, xfds = select.select([stdin], [stdin], fds)
except ValueError, e:
    print "All is well, caught ValueError '%s'." % e
else:
    assert False, "Expected ValueError for write-only fd."
