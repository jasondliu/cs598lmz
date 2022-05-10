import select
# Test select.select

fds = [sys.stdin.fileno()]
timeout = None
result = select.select(fds, [], [], timeout)

print(result)
