import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]='hello'
print lst
'''
'''
import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print 'del',self.name
a=A('a')
d=weakref.WeakValueDictionary()
d['primary']=a
print d['primary'].name
del a
print d['primary'].name
'''
'''
import weakref
class A(object):pass
a=A()
r=weakref.ref(a)
print r
print r()
print r() is a
print r() is None
del a
print r() is a
'''
'''
import weakref
class A(object):pass
a=A()
r=weakref.ref(a,lambda x:print 'object about to be deleted')
print r() is a
del a
print r() is None
'''
'''
import weakref
class A(object):pass
a=A
