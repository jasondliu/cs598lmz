import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(len(lst))
del a
print(len(lst))

#del lst[0]

def f(x):
    x=2
    print(id(x))
a=1
print(id(a))
f(a)
print(id(a))

a=1
def f():
    global a
    a=2
    print(id(a))
print(id(a))
f()
print(id(a))

a=[1,2,3]
b=[4,5,6]
def f():
    a=b
    a[0]=7
    print(a)
f()
print(a)

def f():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
for i in f():
    print(i)

def f():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
a=f()

