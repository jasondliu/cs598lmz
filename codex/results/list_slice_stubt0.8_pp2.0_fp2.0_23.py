import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(str)
weakref.ref(a,callback)
gc.collect()
if len(lst)!=0:raise test_support.TestFailed,\
"callback not called or called with wrong argument"

print 'done'
