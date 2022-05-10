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
print "OK"

# 为了保证程序的正确性，我们需要把所有的引用都清除掉，这样才能确保触发回调
# 也就是说，为了保证回调函数被调用，我们需要删除所有的引用，这样被引用的对象才会被回收
# 所有的引用包括：
# 1.对象自身的引用
# 2.对象的类的引用
# 3.对象的
