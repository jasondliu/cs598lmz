from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4

k = 1
a = array.array('I', [])
for i in range(0, 32):
    a.append(k)
    k = k * 2

n = 0
for j in range(0, 32):
    k = 1
    for i in range(0, 32):
        if a[j] & k:
            print(n)
        k = k * 2
        n = n + 1
