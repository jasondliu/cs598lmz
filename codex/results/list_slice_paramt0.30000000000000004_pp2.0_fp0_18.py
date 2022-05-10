import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print(lst)

#['']

#结论：
#1、弱引用不会增加引用计数，所以不会导致循环引用的问题
#2、弱引用不会增加引用计数，所以不会导致循环引用的问题
#3、弱引用不会增加引用计数，所以不会导致循环引用的问题
#4、弱引用不会增加引用
