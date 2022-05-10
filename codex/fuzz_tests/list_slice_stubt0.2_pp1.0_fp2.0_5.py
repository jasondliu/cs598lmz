import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
print(keepalive)

#[<__main__.A object at 0x00000000029B5C88>]

#在回调函数中删除列表中的元素，会导致回调函数被调用两次，第一次是因为列表中的元素被删除，第二次是因为列表被删除。

#第一次调用回调函数时，列表中的元素被删除，列表中只剩下一个元
