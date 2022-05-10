import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
del a
gc.collect()

def func():
    global lst
    lst.append(str())
    lst[1]=lst[0]
    lst[0]=lst[1]
    del lst[0]
    del lst[1]

def func1():
    global lst
    lst.append(str())
    lst[1]=lst[0]
    lst[0]=lst[1]
    del lst[0]
    del lst[1]

def func2():
    global lst
    lst.append(str())
    lst[1]=lst[0]
    lst[0]=lst[1]
    del lst[0]
    del lst[1]

def func3():
    global lst
    lst.append(str())
    lst[1]=lst[0]
    lst[0]=lst[1]
    del lst[0]
