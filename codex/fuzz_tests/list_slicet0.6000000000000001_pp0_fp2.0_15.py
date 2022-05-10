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
print len(keepali0e)

# 为什么在没有引用的情况下，a的c引用继续存在呢
# 可能是因为，a.c=a 是一个循环引用
# 这个题目跟上面的相似
# 我觉得应该是对象被删除，对象内部还保存着对象本身的引用，导致无法被删除
# 可以看看这个链接
# https://www.cnblogs.com/wuchangqing/p/8120929.html
