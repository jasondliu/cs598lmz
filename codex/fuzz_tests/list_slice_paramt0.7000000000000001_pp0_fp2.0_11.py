import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
print 'lst:',lst

# lst: []

'''

import weakref
class A(object):
    def __del__(self):
        print 'del'
def callback(x):
    print 'callback'
    del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
keepalive.append(weakref.ref(a.c,callback))
del a
del a.c
print 'lst:',lst

# del
# del
# callback
# callback
# lst: []
