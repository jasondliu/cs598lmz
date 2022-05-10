import select
# Test select.select, which currently isn't exposed
from socket import *
from time import time

n = 10000

l = []
for i in range(n):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    l.append(s)

t0 = time()
for i in range(500):
    r, w, x = select.select(l, l, l, 1)
    if i == 0:
        print("size of r, w, x:", len(r), len(w), len(x))
        print("these are not fds, but rather sockets:", repr(r[0]), repr(w[0]), repr(x[0]))
    if not r and not w and not x:
        break
d = time() - t0

print("total time:", d)
print("time per select:", d/500)
print("total events:", n*i)
