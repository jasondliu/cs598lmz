import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#第一个输出为['']，第二个输出为[]
#因为a.c=a，导致a和a.c相互引用，所以没有被回收

#问题2
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#第一个输出为['']，第二个输出为['']
#因为a.c=a，导致
