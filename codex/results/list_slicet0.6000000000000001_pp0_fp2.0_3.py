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
'''

import weakref
import gc

class A(object):
    def __init__(self):
        self.a = self

def callback(x):
    print(x)
    del lst[0]

lst = [str()]
a = A()
a.c = a
keepalive = []
keepalive.append(weakref.ref(a, callback))
del a

while lst:
    keepalive.append(lst[:])
    gc.collect()
