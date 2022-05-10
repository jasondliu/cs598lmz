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
print(lst)

#Q 2.
import weakref
class A(object):
    def __init__(self):
        self.a=1
        self.b=2
    def __del__(self):
        print("delete")
a=A()
keeplst=[]
keeplst.append(weakref.ref(a,lambda x:print("delete")))
del a

#Q 3.
import weakref
class A(object):pass
def callback(x):print("delete")
a=A()
a.a=a
keeplst=[]
keeplst.append(weakref.ref(a,callback))
del a

#Q 4.
import weakref
class A(object):
    def __init__(self):
        self.value=0
    def __del__(self):
        print("delete")
a=A()
keepali0e=[]
keepali0e.append(weakref.ref(a,lambda x:print("delete")))
a.value=12
del a

#Q 5
