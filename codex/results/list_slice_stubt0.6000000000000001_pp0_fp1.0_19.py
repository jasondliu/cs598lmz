import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
print(lst)
del a
print(lst)

import weakref

class A(object):
    def __init__(self,i):
        self.i=i
    def __repr__(self):
        return 'A(%s)'%self.i

def callback(x):
    print('callback',x)
    print(lst)
    print(lst[0]())

keepalive=[]
lst=[str()]
a=A(1)
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print('del a')
print(lst)
del keepalive
print('del keepalive')
print(lst)
lst[0]=A(2)
print('lst[0]=A(2)')
print(lst)
