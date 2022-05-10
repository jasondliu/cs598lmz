from _struct import Struct
s = Struct.__new__(Struct)
s.value = (1, 2, 3)
s.count = 0

x, y, z = s.value

for n in range(3):
    if (n == 0):
        s.value = (x, y+1, z)
    elif (n == 1):
        s.value = (x, y, z+1)
    else:
        s.value = (x+1, y, z)

    s.count = s.count + 1
    for(a, b, c) in s:
        print(s.value)
        print(s.count)
