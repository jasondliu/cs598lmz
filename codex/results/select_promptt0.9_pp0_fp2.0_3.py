import select
# Test select.select().

import select
import os

r, w, x = select.select([0], [1], [2, 3], 2)  # 2.2 raises TypeError here
print r, w, x
print r[0]
print w[0]
print x[0]
print x[1]
