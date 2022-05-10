import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用对象可以被垃圾回收机制回收，而强引用对象不会被回收
# 弱引用对象可以被回收，因此不会产生循环引用
# 弱引用对象可以被回收，因此不会产生循环引用
# 弱引用对象可以被回收，因此不会产生循环引用
# 弱引用对象可以被回收，
