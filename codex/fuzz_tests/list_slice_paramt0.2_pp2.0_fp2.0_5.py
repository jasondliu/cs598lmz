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

#结果：['<__main__.A object at 0x7f6e9c6a5f50>']
#这个例子中，a.c=a，使得a和a.c引用了同一个对象，
#这样，a.c的弱引用就不会被回收，因为a.c的弱引用被a的强引用所持有。
#这里的a.c的弱引用指的是keepalive中的弱引用。
#这个例子中，a.c的弱引用被a的强引用所持有，
#而a的强引
