import select
# Test select.select on a pipe.
r, w = os.pipe()

# Make one end non-blocking.
fl = fcntl.fcntl(r, fcntl.F_GETFL)
fcntl.fcntl(r, fcntl.F_SETFL, fl | os.O_NONBLOCK)

try:
    assert select.select([r], [], [], 0.0) == ([r], [], [])
    assert select.select([r], [], [], 0.0) == ([], [], [])
finally:
    os.close(r)
    os.close(w)
