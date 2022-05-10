import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
def test():
    lst[0]=lst[0]+lst[0]
    if len(lst[0])>10000:
        raise ValueError
def test2():
    try:
        test()
    except ValueError:
        pass
def test3():
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()
    test2()

