import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(keepali0e)
del a
while 1:
    print(lst)
    if not lst:
        break

# ---------------------------------------------------------------------------------------------------------------------
# File "threading_local.py", line 13, in <module>
# ValueError: weak reference to 'thread.local' object under '_threading_local'
# at 0x000002A744C2B100
# ---------------------------------------------------------------------------------------------------------------------

import threading
import _threading_local
import weakref
def callback(x):del lst[0]
lst=[str()]
keepali0e=[]
a=threading.local()
a.b='dd'
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(keepali0e)
del a
while 1:
    print(lst)
    if not lst:
        break

# ---------------------------------------------------------------------------------------------------------------------
# File "threading_local.py", line 28, in <module>
# ValueError: weak reference to 'thread.local' object under
