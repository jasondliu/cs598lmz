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

# 上面的例子中，del lst[0]会被调用，但是del a不会被调用，因为a.c=a会使a不会被回收，
# 因为a.c指向a，而a.c是弱引用，不会影响a的引用计数，所以a不会被回收
# 如果把a.c=a去掉，那么del a也会被调用

# 弱引用的作用：
# 1.防止循环引用
# 2.缓存
# 3.其
