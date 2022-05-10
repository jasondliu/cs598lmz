import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst[:]
for i in range(10):
    if keepali0e:
        print(i,keepali0e[0]())
    else:
        print(i,None)
    for x in range(100):pass



# import gc
# import weakref
#
# lst=[]
#
# class Graph(object):
#     """Demonstrate a cycle, and show that it is collected."""
#     def __init__(self,name):
#         self.name=name
#         lst.append(self.name)
#     def set_next(self,next):
#         print('Linking nodes %s.next = %s' % (self,next))
#         self.next=next
#     def __repr__(self):
#         return '%s(%r)' % (self.__class__.__name__,self.name)
#
# def main():
#     print('Constructing graph')
#     one = Graph('one')
#     two = Graph('
