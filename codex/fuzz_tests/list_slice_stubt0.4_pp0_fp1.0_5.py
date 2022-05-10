import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
gc.collect()
print(lst)

# 注意：
# 如果你要实现一个自定义的弱引用，可以使用 weakref.ref() 来创建它，例如：
# a=A()
# r=weakref.ref(a)
# print(r)
# print(r())
# del a
# print(r())
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print(r() is None)
# print
