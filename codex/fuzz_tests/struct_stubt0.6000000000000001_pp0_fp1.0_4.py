from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

for i in range(100000):
    s.pack(i)

import sys
print(sys.getsizeof(s))
# 4
</code>
I would like to know how is it possible that this structure takes only 4 bytes?


A:

<code>sys.getsizeof()</code> only returns the size of the object itself, and doesn't take into account any other objects that it references.
<code>Struct</code> stores its format string as a <code>str</code> object, and a <code>str</code> object is just a pointer to a memory location.

