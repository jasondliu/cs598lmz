import ctypes
ctypes.cast()  # ???

# In Python 3, range() returns an iterator.
print(list(range(3)))
print(list(range(0, 3)))
print(list(range(0, 10, 3)))
print(list(range(10, 0, -3)))
print(list(range(-10, -100, -30)))

# ?
for i in range(10, 0, -1):
    print('{}'.format(i), end=', ')

print()
for i in range(10, 0, -1):
    print('{}'.format(i), end='')
    if i > 1:
        print(', ', end='')
print()

# ?
for i in range(10, 0, -1):
    print('{}'.format(i), end=', ' if i > 1 else '')

print()

# ?
for i in range(10, 0, -1):
    print('{},'.format(i), end='')

print()
for i in range(10, 0, -1
