import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=a
print('1:',lst,len(keepali0e))
del a
print('2:',lst,len(keepali0e))
del lst
print('3:',lst,len(keepali0e))
print('4:',keepali0e[0](),len(keepali0e))

#防止过早回收
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=a
print('1:',lst,len(keepali0e))
del a
print('2:',lst,len(keepali0e))
del lst
print('3:',lst,len(keepali0e))
print('4:',keepali0e[0](),len(keepali0e))

#回
