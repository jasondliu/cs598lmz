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
print lst
gc.collect()
print lst

#这个例子中，a是一个对象，a.c是a的一个属性，a.c的值是a本身。
#因此，a和a.c引用了同一个对象，这个对象的引用计数是2。
#我们创建了两个弱引用，一个弱引用指向a，另一个弱引用指向a.c。
#当a被删除后，这个对象的引用计
