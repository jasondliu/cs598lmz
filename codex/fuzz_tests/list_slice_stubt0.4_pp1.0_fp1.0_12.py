import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
keepalive.append(lst)
del a
del lst
gc.collect()
print 'ok'

def f():
    for i in range(10):
        yield i

def g():
    for i in range(10):
        yield i

def h():
    for i in range(10):
        yield i

def test_gen():
    l = []
    for x in f():
        l.append(x)
    for x in g():
        l.append(x)
    for x in h():
        l.append(x)
    return l

def test_gen_2():
    l = []
    for x in f():
        l.append(x)
    for x in g():
        l.append(x)
    for x in h():
        l.append(x)
    return l

def test_gen_3():
    l = []
    for x in f():
        l.append(x)
    for x
