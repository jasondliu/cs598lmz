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

# 弱引用的引用对象是一个字典，字典的key是弱引用对象，value是弱引用对象的回调函数，
# 回调函数的参数是弱引用对象的key，回调函数的作用是删除弱引用对象的key，
# 当弱引用对象的key被删除后，弱引用对象自动被回收，
# 当弱引用对象被回收后，弱引用对象的
