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
keepali0e=[]
print('end')
import random
class A():
    def __init__(self,x):
        self.random=random.random()
        self.x=x
def foo():
    lst=[str()]
    while lst:
        if random.random()>5:
            lst.append(A(1))
        elif random.random()>5:
            lst.append(A(2))
        else:
            lst.append(A(3))
        lst=lst[:-1]
print('end')
