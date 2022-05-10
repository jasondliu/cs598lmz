import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print lst

def f(x):
    if x==1:
        raise RuntimeError
    else:
        return x
def g(x):
    try:
        return f(x)
    except RuntimeError:
        return -1
print g(1)
print g(2)

def f(x):
    if x==1:
        raise RuntimeError
    else:
        return x
def g(x):
    try:
        return f(x)
    except RuntimeError:
        return -1
    finally:
        print 'hi'
print g(1)
print g(2)

def f(x):
    if x==1:
        raise RuntimeError
    else:
        return x
def g(x):
    try:
        return f(x)
    except RuntimeError:
        return -1
    finally:
        print 'hi'
print g(1)
print g(2)

def f(x):
    if x==1:
        raise Runtime
