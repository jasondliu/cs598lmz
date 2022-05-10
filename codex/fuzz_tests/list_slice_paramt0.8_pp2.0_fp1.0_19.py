import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]

'''
无论然还否导致回调函数被调用，在Python 3.0中，列表的引用计数减1，从而终止列表的存派。
在Python2.x中，该列表会被视为引用循环，并被保留在内存中。
'''

import sys
def f():
    lst = [1,2,3]
    lst.append(lst)
    return lst
def g():
    lst = f()
    del lst
    return lst
print g()

'''
为了清理引用循环，弱引用
