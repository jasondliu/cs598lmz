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

#这个例子中，a.c=a，这样a就被引用了，不会被回收，所以lst中的str()不会被回收，所以lst不会被清空。
#如果a.c=b，b.c=a，这样a和b互相引用，也不会被回收，lst中的str()也不会被回收。
#如果a.c=b，b.c=c，c.c=a，这样a,b,c互相引用，也不会被回收
