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
g=gc.collect()
print lst,g

a=123
def f():
     global a
     a=321
def f1():
     a=123
f1()
print a
f()
print a

global a
a=1
def f():
     global b
     b=2
print a
b=2
print b

print 1 if True else 2,3


a = []
def f1():
     global a
     a = [1,2]
f1()
print a

a = []
def f1():
     a = [1,2]
f1()
print a

def m1():
    print 'm1'
class class1:
    @staticmethod
    def m1():
        print 'staticmethod m1'
class1.m1()
m1()

def f1():
    print 'f1'
    def f2():
        print 'f2'
    return f2
f1()

class MyClass(object):
    def __new__(cls):
       
