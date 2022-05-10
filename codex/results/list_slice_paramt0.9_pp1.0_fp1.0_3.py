import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst

print type((1,))
print type((1,2))
print type((1,2,3))
print ((1,2,3))

class Foo(object):
    __metaclass__ = MetaClass
    bar = True
print hasattr(Foo, 'bar')
print hasattr(Foo(), 'bar')
f = Foo()
print f.baz()

g = new_attr_class2('a')()
print g.hi()

class A(object):
    def hello(self):
        print "hello, I'm A"
class B(A):
    def hello(self):
        print "hello, I'm B"
def hello(self):
    print "hello, I'm C"
C = type('C', (B,), dict(hello=hello))
#C = type('C', (B,), dict(hello=lambda self:print "hello, I'm C"))
c = C()
c.hello()
print B.__mro__
print C.__mro__

class
