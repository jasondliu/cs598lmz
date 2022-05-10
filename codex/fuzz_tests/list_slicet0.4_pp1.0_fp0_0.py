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
print keepali0e

#第二个例子
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
print keepali0e

#第三个例子
import weakref
class A(object):
    def __init__(self):
        self.x=1
def callback(x):
    print 'object is dead'
a=A()
r=weakref.ref(a,callback)
print r()
del a
print r()

#第四个例子
import weakref
class A(object):
    def __init__(self):
        self.x=1
def callback(x):
    print 'object is dead'
a=A()
r=weak
