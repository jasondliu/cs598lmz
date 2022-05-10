import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append([a,a])
lst.append(weakref.ref(a,callback))
keepali0e.append(lst)
del a
del lst
del keepali0e
#error
'''
'''
import weakref,copy_reg
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=[1,2,3]
lst.append(a)
lst.append(weakref.ref(a,callback))
keepali0e.append(lst)
del a
del lst
del keepali0e
#error
'''
'''
import weakref,copy_reg
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=[1,2,3]
b=a
lst.append(b)
lst.append(weakref.ref(a,callback))
keepali0e.append(lst)
del a
del lst
del keepali0e
#error

