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

#结果：
#['str()']
#[]

#结论：
#当a被删除时，a.c指向a，a.c也被删除，a.c.c指向a.c，a.c.c也被删除，a.c.c.c指向a.c.c，a.c.c.c也被删除，
#a.c.c.c.c指向a.c.c.c，a.c.c.c.c也被删除，a.c.c.c.c.c指向a.c.c.c.c，a.c.c.c
