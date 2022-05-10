import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
del a
for i in range(5):
    print(lst)
#str()
#str()
#str()
#str()
#str()

class A(object):
    def __init__(self):
        self.c=self
    def __del__(self):
        print("del")
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a.c,callback))
lst[0]=a
del a
for i in range(5):
    print(lst)
#del
#[]
#[]
#[]
#[]
#[]

class A(object):
    def __init__(self):
        self.c=self
        self.d=1
    def __del__(self):
        print("del")
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(
