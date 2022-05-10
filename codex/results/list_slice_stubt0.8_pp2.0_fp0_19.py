import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
while lst:del a

def func(arg):
    if arg==1:
        func(arg+1)
    else:
        func(arg-1)
func(1)

def func():
    for i in xrange(10000000):
        yield i
g=func()
while True:
    try:
        g.next()
    except StopIteration:
        break

def func(x):
    if x in [1,2]:
       func(x+1)
    else:
        func(x-1)
func(1)

def func(x):
    for i in xrange(x):
        for i in xrange(x):
            pass
func(50000)

def func():
    return func()
func()

class A:
    def __del__(self):
        self.a=self
a=A()
del a
