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

#在Python3.4.3中，输出结果为：
#['']
#在Python2.7.10中，输出结果为：
#[]
#结论：
#Python3.4.3中，可以看到，对象a和a.c是相互引用的，但是在Python3.4.3中，当对象a被删除后，a.c依然存在，因此，在Python3.4.3中，a.c是一个
