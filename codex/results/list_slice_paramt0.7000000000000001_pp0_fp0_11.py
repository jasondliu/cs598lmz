import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a=None
print lst[0]

from weakref import WeakValueDictionary
mydict=WeakValueDictionary()
mydict['a']=1
mydict['b']=2
mydict['c']=3
print mydict
del mydict['a']
del mydict['b']
del mydict['c']
print mydict

import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a.c,lst.pop))
a=None
print lst

from weakref import WeakKeyDictionary
mydict=WeakKeyDictionary()
mydict[1]=1
mydict[2]=2
mydict[3]=3
print mydict
del mydict[1]
del mydict[2]
del mydict[3]
print mydict

def get_callback(x):
    def callback(reference):
        print 'calling back with',reference.x
    return callback
class MyClass(object):
    def
