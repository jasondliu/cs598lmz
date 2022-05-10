import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(id(keepali0e[0]) in list(map(id,gc.get_referrers(a))))
del a
print(lst)

#!/usr/bin/env python
# coding=utf-8
class Base(object):
    def __del__(self):
        print('Base.__del__')
class A(Base):pass
class B(Base):pass
def test():
    a=A()
    b=B()
    print('in test()')
if __name__=='__main__':
     test()

#!/usr/bin/env python
# coding=utf-8
import weakref
class A(object):pass
a=A()
print(id(a))
print(type(a))
wr=weakref.ref(a)
print(id(wr))
print(type(wr))


#!/usr/bin/env python
# coding=utf-8
import weakref
class A(object):
    def __init__(self,name):
        self.name=name
   
