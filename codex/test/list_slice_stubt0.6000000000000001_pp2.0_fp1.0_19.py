import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(lst)
del a
lst.append(1)
del lst[0]

#print(lst)
#print(keepali0e)

"""
"""
class Foo(object):
    def __init__(self):
        print('__init__')
    def __del__(self):
        print('__del__')

a = Foo()

b = a

c = b

"""
"""
class Foo(object):
    def __init__(self):
        print('__init__')
    def __del__(self):
        print('__del__')

def goo():
    a = Foo()
    b = a
    c = b
    print('in goo')

goo()
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(lst)
#del a
lst.append(1)
del lst
