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
print(len(keepali0e))

# 这个例子的输出是多少？
# 你可以认为它是一个无限循环，但实际上不是。
# 你可以认为它会持续运行直到内存耗尽，但实际上不是。
# 它的输出是一个整数，比如：
#
# >>> len(keepalive)
# 5
#
# 注意，这里的输出可能会有所不同，这取决于你的 Python 实现。
#
# 这个例子是怎么回
