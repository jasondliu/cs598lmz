from _struct import Struct
s = Struct.__new__(Struct)
s.size = 4
s.format = 'i'
a = array('i', list(range(10)))  # int array
print(s.pack(42), s.pack(1729))
print(s.pack_into(a, 0))

print(s.unpack(a))
print(s.unpack_from(a, 4))

# Task 3 - I can't believe it's not mutating!
a = array('i', [3, 6, 9, 12, 15])
b = array('i')
b.extend(a[1:-1])
print(b)

# Task 4 - The killer Nack!
a = array('H', [4000, 10, 700, 22222])
print("a[1:3]: {}".format(a[1:3]))

# Task 5 - Spend an afternoon with NumPy
# a = (1, 2, 3, 4)
# b = (3, 4, 5, 6)
#
# for i, j in map(None, a, b):
#     print(i, j)
