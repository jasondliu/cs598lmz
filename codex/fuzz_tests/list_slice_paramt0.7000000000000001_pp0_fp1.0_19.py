import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print (a.c is None)
print (a is None)
'''

#weakref.finalize(obj,func,*,args,kwargs)
'''
import weakref
class A(object):pass
def callback(x):print ('callback')
a=A()
weakref.finalize(a,callback)
print (a)
del a
'''

#weakref.proxy(object[,callback])
'''
import weakref
class A(object):pass
a=A()
b=weakref.proxy(a)
print (b)
'''

#weakref.getweakrefs(object)
'''
import weakref
class A(object):pass
a=A()
b=A()
b.c=a
keepali0e=[]
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(b))
print (weakref.getweakrefs(a))
