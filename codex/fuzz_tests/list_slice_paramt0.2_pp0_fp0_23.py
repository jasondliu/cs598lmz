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

#结果：['\x00']
#结论：当删除a时，a.c引用a，a.c引用a，a引用a.c，a引用a.c，a.c引用a，a.c引用a，a引用a.c，a引用a.c，a.c引用a，a.c引用a，a引用a.c，a引用a.c，a.c引用a，a.c引用a，a引用a.c，a引用a.c，a.c引用a，a.c引用a，a引
