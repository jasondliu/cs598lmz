from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<250I"
print(s.size)

# 3
import os

print(os.getcwd())
os.chdir('/root/')
print(os.getcwd())

# 4
import math

s = math.pi
s = s ** 0.5
s = s ** 0.5
s = s ** 0.5
print(s)

# 5

x = ['0', '1', '2', '3', '4']
z = x[::2]
z = ''.join(z)
z = int(z)
print(z)

# 6

data = [1, 2, 3, 4, 5]
d = data[1]
d = data[3]
print(d)

# 7

data = 'abcdef'
d1 = int(data[3:5], 16)
print(d1)

# 8
