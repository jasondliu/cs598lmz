import select
# Test select.select()
r, w, x = select.select([], [1], [], 0)
print(r)
print(w)
print(x)

r, w, x = select.select([1], [], [], 0)
print(r)
print(w)
print(x)

r, w, x = select.select([1], [1], [], 0)
print(r)
print(w)
print(x)

r, w, x = select.select([1], [1], [1], 0)
print(r)
print(w)
print(x)

r, w, x = select.select([1], [1], [1], 0.1)
print(r)
print(w)
print(x)

# Test select.poll()
p = select.poll()
p.register(1, select.POLLIN)
r = p.poll(0)
print(r)
r = p.poll(0.1)
print(r)

# Test select.epoll()
e = select.ep
