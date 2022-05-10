import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print("id a:%s"%id(a))
del a
wr=weakref.ref(lst[0],callback)
print("id callback(wr):%s"%(id(wr)))
print("%s"%(id(lst)))
print("id lst[0]:%s"%id(lst[0]))
del lst
# as lst-memory has been free, wr-reference cant return lst's address
print("%s"%(wr))
print(keepalive)
