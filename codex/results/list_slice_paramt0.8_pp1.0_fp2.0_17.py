import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print lst,len(lst)
del a
for i in range(100):
    print i,lst,len(lst)
    if len(lst)==0:break
print '******',lst,len(lst)
