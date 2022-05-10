import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del lst[0]
del keepali0e[0]
gc.collect()
print keepali0e
print lst

#全局变量被引用后，可以在gc时调用callback
print "global"
lst=[str()]
keepali0e=[]
def callback(x):
    del lst[0]
def func():
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    lst.append(a)
    del a
func()
del lst[0]
del keepali0e[0]
gc.collect()
print keepali0e
print lst


#局部变量不被引用，则callback不会被调用
print "local"
def func():
    lst=[str()]

