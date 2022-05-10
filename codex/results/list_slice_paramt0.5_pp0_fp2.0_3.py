import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#['']
#[]

# 弱引用可以被用于跟踪对象的创建与销毁情况，而不会影响对象的生命周期。
# 弱引用可以用来解决循环引用的问题。
# 弱引用可以被用于实现缓存。
