import select
# Test select.select for a timeout of 0.
# This is needed on some systems to make sure that
# "select" doesn't modify the timeout variable.
# This test is copied from test_socket.

import select
import time

for timeout in (0, 0.0):
    start = time.time()
    r, w, x = select.select([], [], [], timeout)
    elapsed = time.time() - start
    assert r == w == x == [], (r, w, x)
    assert 0.0 <= elapsed < 0.5, elapsed
