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

# 分析：
# 回调函数可以在弱引用对象被回收时执行。
# 实际上，回调函数是在引用计数为0时执行。
# 这里的回调函数是删除列表的第一个元素。
# 当a被回收时，回调函数删除了lst的第一个元素，
# 因此lst变为空列表，while循环结束。
# 这里有个问题，
