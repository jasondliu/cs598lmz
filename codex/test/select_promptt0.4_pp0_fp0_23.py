import select
# Test select.select() with a timeout

import select, time

def test():
    timeout = 1.0
    r, w, x = select.select([], [], [], timeout)
