import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=a
del a
for i in range(100):
    d=weakref.WeakKeyDictionary(callback)
    del d
''',["ReferenceError: weakly-referenced object no longer exists" if not mode.startswith('--jython') else None])
    test('''
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(a)
del a
for i in range(100):
    d=weakref.WeakValueDictionary()
    d[i]=lst[0]
    del d
''',["ReferenceError: weakly-referenced object no longer exists" if not mode.startswith('--jython') else None])
