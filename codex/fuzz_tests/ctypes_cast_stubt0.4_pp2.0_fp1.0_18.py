import ctypes
ctypes.cast(id(x), ctypes.py_object).value

print(x)
print(y)

# 2.2
# a.
print(2**38)

# b.
print(''.join([chr(ord('a') + i) for i in range(26)]))

# c.
print('map'.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))

# d.
print(''.join([chr(ord('a') + i) for i in range(26)]).translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))

# e.
print(''.join([chr(ord('a') + i) for i in range(26)]).translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmn
