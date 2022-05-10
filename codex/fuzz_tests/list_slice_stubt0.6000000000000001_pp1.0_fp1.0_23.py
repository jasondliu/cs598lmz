import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
gc.collect()
print gc.collect()
print lst

#
#class Node(object):
#    def __init__(self,value):
#        self.value=value
#        self.prev=None
#        self.next=None
#
#class DoubleLinkedList(object):
#    def __init__(self):
#        self.head=None
#        self.tail=None
#
#    def insert(self,node):
#        if self.head is None:
#            self.head=node
#            self.tail=node
#        else:
#            self.tail.next=node
#            node.prev=self.tail
#            self.tail=node
#
#    def remove(self,node):
#        if node.prev is not None:
#            node.prev.next=node.next
#        else:
#            self.head=node.next
#        if node.next is not None:
#            node.next.prev=node
