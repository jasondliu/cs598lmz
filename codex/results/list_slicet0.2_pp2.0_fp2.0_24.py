import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e

#这个例子中，a.c=a，导致a和a.c互相引用，因此a不会被回收，而a.c是一个弱引用，因此a.c会被回收，而a.c被回收后，callback函数被调用，callback函数中del lst[0]，导致lst[0]被删除，因此lst变为空，while循环结束，最后输出keepali0e，keepali0e中的第一个元素是一个弱引用，
