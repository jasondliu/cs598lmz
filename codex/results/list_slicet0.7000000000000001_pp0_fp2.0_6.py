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

#The above code will cause a memory leak,but Python 2.6.5+ will print
#"Exception RuntimeError: 'cannot create weak reference to
#     <class '__main__.A'>: attribute lookup __weakref__ on __main__.A
#     failed'"

#(c)memory leak
import weakref
lst=[]
class A(object):
    def __init__(self,a):
        self.a=a
        lst.append(weakref.WeakKeyDictionary(self))
    def func(self):
        lst.append(self.a)
a=A(1)
a.func()
del a
while lst:lst.pop()

#(d)memory leak
import weakref
lst=[]
class A(object):pass
def callback(x):lst.append(x)
a=A()
a.c=a
weakref.ref(a,callback)
del a
while lst:lst.pop()

#(e)memory leak
import weakref
class A(object
