import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback=callback))
print(lst)

# 在创建弱引用时候，先创建回调函数，再用回调函数创建弱引用，这样一来弱引用就能被提前回收，即使引用被赋值给一个对象的成员变量，也能保证回调函数执行

# 将两个引用的对象的引用赋值给两个列表，第一个引用的对象的引用被回收，这
