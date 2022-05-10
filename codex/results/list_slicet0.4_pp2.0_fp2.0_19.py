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
print(lst)

#下面的程序是一个更复杂的例子，它利用一个缓存来保存最近使用过的数据项，并且每次访问数据项的时候，都会把它移动到缓存的最前面。
#这个缓存是一个有序列表，并且它的大小是有限制的。当缓存满了之后，就会把最旧的数据项删除掉。
#本质上，
