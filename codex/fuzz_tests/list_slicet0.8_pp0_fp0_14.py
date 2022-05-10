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
#对于没有弱引用的对象，还有一个解决方案：可通过响应对象自身的__del__方法解除引用。这在解除两个相互引用的对象时非常有用。
class Node(object):
    def __init__(self,value):
        self._value=value
        self._children=[]
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            for x in c.depth_first():
                yield
