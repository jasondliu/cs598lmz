import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from pwn import *

context.log_level = 'debug'

p = process('./pwn')

def add(size, content):
    p.recvuntil('Your choice:')
    p.sendline('1')
    p.recvuntil('Size:')
    p.sendline(str(size))
    p.recvuntil('Content:')
    p.send(content)

def show(index):
    p.recvuntil('Your choice:')
    p.sendline('2')
    p.recvuntil('Index:')
    p.sendline(str(index))

def delete(index):
    p.recvuntil('Your choice:')
    p.sendline('3')
    p.recvuntil('Index:')
    p.sendline(str(index))

def exit():
    p.recvuntil('Your choice:')
    p.sendline('4')

add(0x80, 'a')
