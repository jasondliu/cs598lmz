import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
keepalive=a_wr,lst
del a
print len(lst)
keepalive=None
print len(lst)

"""
输出：

1
0
"""
