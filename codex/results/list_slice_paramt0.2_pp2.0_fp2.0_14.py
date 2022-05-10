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

#结果：['1']

#结论：
#1、当对象a被删除时，a.c被删除，a.c.c被删除，a.c.c.c被删除，以此类推，直到没有循环引用的对象，这些对象才会被删除
#2、当对象a被删除时，a.c被删除，a.c.c被删除，a.c.c.c被删除，以此类
