import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e)
print len(lst)
del a
print len(keepali0e)
print len(lst)

"""
output:
1
1
0
0
"""
