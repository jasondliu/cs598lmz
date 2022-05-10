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
</code>
Gdb print:
<code>Program received signal SIGSEGV, Segmentation fault.
0x081e13bf in _PyWeakref_GetWeakrefCount () at Objects/weakrefobject.c:414
414     if (!wr)
(gdb) bt
#0  0x081e13bf in _PyWeakref_GetWeakrefCount () at Objects/weakrefobject.c:414
#1  0x081e1403 in _PyWeakref_GetWeakrefCount () at Objects/weakrefobject.c:422
#2  0x081e07f9 in call_c_callback () at Objects/weakrefobject.c:350
#3  0x081e0863 in collect () at Objects/weakrefobject.c:363
#4  0x081e0a5a in call_c_callback () at Objects/weakrefobject.c:393
#5  0x081e08cf in collect () at Objects/weakrefobject.c:365
#6  0x081dfb1e in _PyWeak
