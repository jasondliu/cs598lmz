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

# 一个稍微复杂点的例子，这个例子中，我们创建了一个循环引用，然后通过弱引用来删除这个循环引用。
# 在这个例子中，我们创建了一个类A，然后创建一个实例a，并且让a.c=a，这样就创建了一个循环引用。
# 然后我们创建了一个列表lst，并且在列表中添加一个字符
