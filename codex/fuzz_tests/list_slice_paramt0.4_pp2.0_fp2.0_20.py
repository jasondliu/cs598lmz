import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

# 这个例子，通过weakref.ref()创建了一个弱引用，并将其绑定到a上，当a被删除的时候，会调用callback()函数，callback()函数会删除lst[0]，这样就会触发lst[0]的__del__方法，这个例子就是在演示，如果在__del__方法中，调用了一个需要gc回收的对象，会导致gc不能回收这个对象，
