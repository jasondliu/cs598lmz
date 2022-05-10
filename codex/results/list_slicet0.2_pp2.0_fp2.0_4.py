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

#链表
class Node(object):
    def __init__(self,value=None,next=None):
        self.value,self.next=value,next
    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value,self.next)
    __repr__=__str__

class LinkedList(object):
    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        node=Node()
        self.root=node
        self.tailnode=node
        self.length=0
    def __len__(self):
        return self.length
    def append(self,value):
        if self.maxsize is not None and len(self)>=self.maxsize:
            raise Exception('LinkedList is Full')
        node=Node(value)
        tailnode=self.tailnode
        tailnode.next=node
        self.tailnode=node
        self.length+=1
    def appendleft(self,value
