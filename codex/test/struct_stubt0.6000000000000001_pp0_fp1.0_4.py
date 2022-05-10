from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

for i in range(100000):
    s.pack(i)

import sys
print(sys.getsizeof(s))
# 4
