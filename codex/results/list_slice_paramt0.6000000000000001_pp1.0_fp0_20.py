import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst

a=None
print lst



import time
import weakref
class C(object):
    def __del__(self):
        print 'I am dying'
c=C()
r=weakref.ref(c,lambda x:print 'c is dead')
del c
print r()
time.sleep(1)
