import select
# Test select.select() behavior regarding a write-only file descriptor.
fds = []
stdin = sys.stdin.fileno()
fds.append(stdin)
