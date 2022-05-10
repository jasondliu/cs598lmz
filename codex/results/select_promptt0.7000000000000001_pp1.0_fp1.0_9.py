import select
# Test select.select
rlist = [sys.stdin]
wlist = []
xlist = []
r, w, x = select.select(rlist, wlist, xlist)
print('r =', r)
print('w =', w)
print('x =', x)

# Test select.poll
p = select.poll()
p.register(sys.stdin.fileno(), select.POLLIN)
for fd, event in p.poll():
    print('fd =', fd)
    print('event =', event)

# Test select.epoll
e = select.epoll()
e.register(sys.stdin.fileno(), select.EPOLLIN)
for fd, event in e.poll():
    print('fd =', fd)
    print('event =', event)
