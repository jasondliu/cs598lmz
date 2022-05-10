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

# 可以将一个对象的引用加入到列表中，这样就可以避免在回收时调用回调函数。
# 因为对象的强引用也被列表所持有，所以不会被回收。
# 在Python解释器退出时，对象才会被回收，此时回调函数会被调用。
# 因为Python解释器会自动回收强引用列表中的对象，所以列表中的对
