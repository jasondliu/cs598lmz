import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(str())
keepali0e.append(str())
del keepali0e
lst[0]

class C(object):
    def __init__(self,x=0):
        self.x=x
    def __lt__(self,other):
        return self.x < other.x
    def __eq__(self,other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class D(object):
    def __init__(self,x=0):
        self.x=x
    def __lt__(self,other):
        return self.x < other.x
    def __eq__(self,other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

items = [C(1), C(2), D(3), D(4), D(5)]
s = set(items)
for i in xrange(len(items
