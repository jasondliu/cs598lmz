import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "len(keepali0e)",len(keepali0e)
print "len(lst)",len(lst)
print "str()",str()
print "str()==str()",str()==str()
print "str(lst[0])",str(lst[0])
print "str(lst[0])==str()",str(lst[0])==str()
print 'str(lst[0])==str(lst[0])',str(lst[0])==str(lst[0])
del a
assert len(lst)==0
