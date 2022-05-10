import select
# Test select.select() with a zero timeout

import select, time

def test_select_timeout(maxdelay):
    "test select with a timeout"
    r, w, x = select.select([], [], [], 0)
    assert r == w == x == []
    start = time.time()
    r, w, x = select.select([], [], [], maxdelay)
    assert r == w == x == []
    delay = time.time() - start
    assert 0.0 <= delay <= 2.0*maxdelay, \
           "Timeout too small or too big: %s" % delay

test_select_timeout(0.1)
