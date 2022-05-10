import select
# Test select.select() with a timeout

import select
import time

def test_select_timeout():
    # select.select() should return 3 empty lists after the timeout
    r, w, x = select.select([], [], [], 0.1)
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0

def test_select_timeout_early_wakeup():
    # select.select() should return 3 empty lists after the timeout
    # even if the timeout is woken up early
    start = time.time()
    r, w, x = select.select([], [], [], 0.1)
    duration = time.time() - start
    assert duration < 0.1
    assert len(r) == 0
    assert len(w) == 0
    assert len(x) == 0

def test_select_timeout_negative():
    # select.select() should raise ValueError if the timeout is negative
    try:
        select.select([], [], [], -1)
    except ValueError:
        pass
    else
