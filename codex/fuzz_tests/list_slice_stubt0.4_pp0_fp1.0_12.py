import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst

#如果把a.c=a注释掉，那么程序将会在del a的时候报错，因为a被回收了，但是lst里面还有a的引用，所以还会调用callback函数，callback里面的del lst[0]就会报错了。
#但是如果a.c=a，那么a就不会被回收，因为a.c=a，a.c指向a，a指向a.c，所
