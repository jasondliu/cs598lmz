import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
weakref.ref(a,callback)
del a
keepali0e[0].c= keepali0e[0]
#del lst
gc.collect()
print lst
# 第7个test
print "test7"
class Graph(object):
    def __init__(self,name):
        self.name=name
        self.next=None
    def set_next(self,next):
        print 'Linking nodes %s.next=%s' % (self,next)
        self.next=next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,self.name)
class Node(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__,self.name)
one=Graph('one')
two=Graph('two')
one.set_next
