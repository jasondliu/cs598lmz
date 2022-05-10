import select
# Test select.select() for timeout < 0 (should return immediately)

import select

for timeout in [-1, -2, -100, select.EPOLLET]:
    (r, w, x) = select.select([], [], [], timeout)
    print r, w, x
