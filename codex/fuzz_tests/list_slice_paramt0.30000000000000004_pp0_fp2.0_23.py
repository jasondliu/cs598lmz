import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print len(lst)

# 下面这个例子是演示弱引用的一个应用，可以维护一个大的数据结构，并且可以在不需要的时候自动释放内存。
# 在这个例子中，我们使用了一个字典，字典的键是一个字符串，值是一个弱引用，弱引用的目标是一个列表。
# 当一个列表不再被引用的时候，它会自动
