import select
# Test select.select() with timeout = None

r,w,x = select.select([1], [], [], None)
print(r)
print(r[0])
r,w,x = select.select([], [1], [], None)
print(w)
print(w[0])
r,w,x = select.select([], [], [1], None)
print(x)
print(x[0])

# Test select.select() with timeout = 0

try:
    r,w,x = select.select([1], [], [], 0)
    print(r)
    print(r[0])
except select.error as e:
    print('caught', e)
r,w,x = select.select([], [1], [], 0)
print(w)
print(w[0])
r,w,x = select.select([], [], [1], 0)
print(x)
print(x[0])

# Test select.select() with timeout > 0

import time
start = time.time()
r,w
