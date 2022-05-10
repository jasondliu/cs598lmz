import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
a_key=a
keepali0e.append(a_key)
lst.append(a_key)
del a_key
del a
gc.collect()
def an_anonymous_ref_to(x):
    return weakref.ref(x,callback)
ref_to_a=an_anonymous_ref_to(keepali0e[1][1])
try:
    print(ref_to_a())
    print(lst)
except:
    print("只有第一个元素的列表")
    print(lst)
