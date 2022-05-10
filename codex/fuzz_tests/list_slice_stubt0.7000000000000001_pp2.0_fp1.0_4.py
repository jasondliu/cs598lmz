import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
lst.append(A())
lst.append(A())
a=A()
a.c=a
lst.append(a)
lst[-1].c=lst[-1]
keepalive.append(lst[0])
keepalive.append(lst[1])
keepalive.append(lst[2])
keepalive.append(lst[3])
del a
keepalive.append(lst[0].c)
del lst
"""

import weakref

class A(object): pass

def callback(x):
    del lst[0]

keepalive = []

lst = [str()]

a = A()
a.c = a
lst[0] = a
lst.append(A())
lst.append(A())
a = A()
a.c = a
lst.append(a)
lst[-1].c = lst[-1]

keepalive.append(lst[0])
