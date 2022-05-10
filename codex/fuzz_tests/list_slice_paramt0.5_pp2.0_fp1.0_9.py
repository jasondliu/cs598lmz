import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(100):
    a=A()
    a.c=a
    lst.append(a)
    keepali0e.append(weakref.ref(a,callback))
    del a
    if not lst:
        break
print(i)

#6
import weakref
class A(object):
    def __del__(self):
        print("A.__del__")
    def __repr__(self):
        return "A instance"
a=A()
r=weakref.ref(a)
print(r)
print(r())
del a
print(r())

#7
import weakref
class A(object):
    def __del__(self):
        print("A.__del__")
    def __repr__(self):
        return "A instance"
a=A()
r=weakref.ref(a)
print(r)
print(r())
a=1
print(r())

#8
import weakref
class A(object):
