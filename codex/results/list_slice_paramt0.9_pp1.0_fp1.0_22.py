import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=A()
b.c=b
keepali0e.append(weakref.ref(b,callback))
del a,b
def run():
    str()*len(keepali0e)
    i=-(-3)
run()
