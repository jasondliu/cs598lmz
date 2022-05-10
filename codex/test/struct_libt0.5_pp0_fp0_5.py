import _struct

from pwn import *

#context.log_level = 'debug'

r = remote('pwn.chal.csaw.io', 8001)

#r = process('./rop')

e = ELF('./rop')

#libc = e.libc

#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

libc = ELF('/lib/i386-linux-gnu/libc.so.6')

#gdb.attach(r, '''

