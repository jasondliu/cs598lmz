import select
# Test select.select with an empty list of fds.
select.select([], [], [])

# Test select.select with a list containing None.
select.select([None], [None], [None])

# Test select.select with a write_only fd.
r, w, x = select.select([], [1], [])
r, w, x = select.select([], [sys.stdout], [])
r, w, x = select.select([], [sys.stdout.fileno()], [])

# Test select.select with a read_only fd.
r, w, x = select.select([0], [], [])
r, w, x = select.select([sys.stdin], [], [])
r, w, x = select.select([sys.stdin.fileno()], [], [])
