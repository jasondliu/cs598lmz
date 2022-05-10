import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]

#这个案例虽然不是很明白，但是还是很棒的，可以让我们了解一个知识点，就是弱引用
