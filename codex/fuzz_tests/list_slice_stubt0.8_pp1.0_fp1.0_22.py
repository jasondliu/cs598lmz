import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
a=None
del a
del keepalive[0]
callback(None)
print(lst)
'''

#test2.3

'''
#coding:utf-8
import weakref,gc
class A(object):pass
a=A()
a.d=a
keepalive=[]
a_wr=weakref.ref(a)
keepalive.append(a)
m=weakref.WeakKeyDictionary()
m['A']=a
m['A_wr']=a_wr
print(m['A'])
print(m['A_wr'])
del a
del a_wr
del m
del keepalive
gc.collect()
print(a)

'''

#test2.4
'''
import weakref
class A(object):pass
a=A()
c=A()
a.b=c
c.d=a
keepalive=[]
keepalive.append
