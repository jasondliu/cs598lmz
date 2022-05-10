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
gc.collect()
print(keepalive)

#这个例子中，lst是一个列表，它的第一个元素是一个字符串，第二个元素是一个弱引用，它引用的是lst本身。
# 当lst被删除时，弱引用会被调用，它会删除lst的第一个元素。
# 然而，由于lst的第一个元素是一个字符串，它不会被
