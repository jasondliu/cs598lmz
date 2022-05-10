import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#这个例子中，a.c=a，这个循环引用会导致a不会被回收，因此lst中的字符串对象也不会被回收。
#如果把a.c=a这句话注释掉，那么a就会被回收，因此lst中的字符串对象也会被回收。
#这个例子中，a.c=a，这个循环引用会导致a不会被回收，因此lst中的字
