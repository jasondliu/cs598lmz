from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i", "test")

print("test", s.size)
print(s.unpack(b'\x00\x00\x00\x00'))
```

```
test 4
(0,)
```

---

### Memoryview

```
from array import array
from binascii import hexlify
from _struct import Struct

numbers = array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast("B")
print(hexlify(memv_oct.tobytes()))

memv_oct[5] = 4
print(numbers)

```

```
5
-2
b'feff00000100'
array('h', [-2, -1, 1024, 1, 2])
```

---

### 字节序

```
import sys
import bin
