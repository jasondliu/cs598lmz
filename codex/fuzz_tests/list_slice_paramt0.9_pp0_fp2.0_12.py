import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
memary_ref=lst[0]
print(a)


import sys
import weakref
class A(object):
    def __init__(self,x):
        self.x=x
def callback(x):
    print(x)
a=A(42)
ref=weakref.ref(a,callback)

del a
print(sys.getrefcount(ref))
print(type(ref))
print(ref())
print(ref is None)
print(ref() is None)
print(ref.x)
try:
    print(ref())
except ReferenceError as err:
    print('dead,blue and broken',err)
class A(object):pass
a=A()
ref=weakref.ref(a)
try:
    del ref
except NameError as err:
    print(err)
try:
    del ref
except Exception as err:
    print(err)
