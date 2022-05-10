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
print(lst)

class Node(object):
    def __init__(self,value):
        self.value=value
        self._parent=None
        self.children=[]
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
    def add_child(self,node):
        self.children.append(node)
        node._parent=self
    def remove_child(self,node):
        self.children.remove(node)
        node._parent=None
    def __iter__(self):
        return iter(self.children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


root=Node(0)
child1=Node(1)
child2=Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5
