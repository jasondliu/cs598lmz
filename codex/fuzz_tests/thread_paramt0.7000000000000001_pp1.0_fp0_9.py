import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

# create a box
b = box.Box([10, 9, 8, 7, 6], names=('a', 'b', 'c', 'd', 'e'))
print(b)

# add an array
b['f'] = np.arange(10)

print(b)

# you can also slice
print(b['a':'c'])

# or select based on the values
print(b[b > 6])

# or use boolean arrays
print(b[np.array([0, 0, 0, 1, 1])])

# add another box
b2 = box.Box(np.random.randn(10, 3), names=('one', 'two', 'three'))

# you can concatenated boxes with hstack
c = box.hstack((b, b2))
print(c)

# or vertically with vstack
d = box.vstack((b.T, b2.T))
print(d)

# you can also create new boxes out of existing ones

