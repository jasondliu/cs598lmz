import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)
print("{}".format("".join(map(str,keepali0e))))
"""

import gc
def a(n):
    if n==0:
        return str()
    lst=a(n-1)
    if n<29:
        lst+=str(n)
    print(list(gc.get_referrers(lst)))
    return lst
print(a(28))
1
