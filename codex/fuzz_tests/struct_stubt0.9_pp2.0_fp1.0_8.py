from _struct import Struct
s = Struct.__new__(Struct)
#s._update_format_string
s.format = 'I'
s.size = 4
s.pack(1)

print hash(tuple([2, 3]))
print hash(tuple([1, 2]))
print hash((1, 2))
print hash(tuple([3, 2]))

for i in range(10):
    print i
    if i == 8:
        break
