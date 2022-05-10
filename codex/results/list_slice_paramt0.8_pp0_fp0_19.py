import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a

class A:
    def __init__(self, x):
        self.x=x

    def __del__(self):
        print(self.x)

a=A(1)
b=A(2)
a.b=b
b.a=a
del a, b

class A:
    def __init__(self):
        self.a=self.b=self

    def __del__(self):
        print("destructor")
        del self.a, self.b

keepalive=[]
for i in range(10):
    a=A()
    keepalive.append(a)
del keepalive

class A:
    def __init__(self):
        self.a=self.b=self

    def __del__(self):
        print("destructor")
        del self.a

keepalive=[]
for i in range(10):
    a=A()
    keepalive.append(a)
del keepalive

class A:

