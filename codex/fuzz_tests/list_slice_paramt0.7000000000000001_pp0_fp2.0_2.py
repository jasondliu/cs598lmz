import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while keepali0e:
    lst.append(lst[0])
    keepali0e.pop()
    del lst[0]
    gc.collect()
    print(lst)
#在标准的Python实现中，内存溢出。



#import weakref
#class A(object):pass
#def callback(x):pass
#keepali0e=[]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#del a
#while keepali0e:
#    lst.append(lst[0])
#    keepali0e.pop()
#    del lst[0]
#    gc.collect()
#    print(lst)
#在标准的Python实现中，内存溢出。

#import weakref
#class A
