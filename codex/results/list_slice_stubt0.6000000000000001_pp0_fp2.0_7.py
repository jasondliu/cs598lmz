import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(lst[0],callback))

#print(lst)
#print(keepali0e)

#import gc
#gc.collect()

#print(lst)
#print(keepali0e)

#print(gc.collect())

#print(lst)
#print(keepali0e)

#a=None
#print(gc.collect())

#print(lst)
#print(keepali0e)

#lst=None
#print(gc.collect())

#print(lst)
#print(keepali0e)

#print(gc.collect())

#print(lst)
#print(keepali0e)

#del keepali0e[0]
#print(gc.collect())

#print(lst)
#print(keepali0e)

#print(gc.collect())

#print(lst)
#print(keepali0e)

#l
