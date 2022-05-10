import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
if (not(lst)):lst=[str()]
del lst[0]
if (not(lst)):lst=[str()]
print len(lst)
# def callback(x):del lst[0]
# keepalive=[]
# lst=[""]
# a=A()
# a.c=a
# keepalive.append(a)
# if(not(lst)):lst=[""]
# weakref.ref(a, callback)
# if(not(lst)):lst=[""]
# print len(lst)
