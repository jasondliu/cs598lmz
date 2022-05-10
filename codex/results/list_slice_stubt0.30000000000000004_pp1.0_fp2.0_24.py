import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
print(lst)
del a
print(lst)
print(w)
print(w())
print(lst)

#结果：
#['\x00']
#['\x00']
#<weakref at 0x0000020E4B4C7E08; dead>
#None
#['\x00']

#结论：
#当对象a被回收时，回调函数callback被调用，但是由于a.c=a，导致a不能被回收，因此w()返回None，但是回调函数callback被调用，lst的第一个元素被
