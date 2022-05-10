import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=A()
b.a=a
b.c=a
keepali0e.append(weakref.ref(b,callback))
x=b.a.c
lst[0]
a.c=a
b.c=a
b.a=a
lst

# __slots__
__slots__=()
__slots__=("a","b",)
class C(object):
	__slots__=("a","b",)
	def __init__(self):self.a=1

c=C()
c.a
c.b

class D(C):
	__slots__=("c","d",)
	def __init__(self):
		C.__init__(self)
		self.c=2

d=D()
d.a
d.b
d.c
d.d

assert issubclass(D,C)

# __init__ 的调用
class X(object):pass
x=X()


