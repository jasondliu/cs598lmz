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
print(keepali0e)

#这个程序的输出是什么？
#程序的输出是一个空列表，因为在程序中，a.c=a，这样a引用自身，导致a不会被回收，而a是lst[0]的弱引用，所以lst[0]不会被回收，所以lst不会被回收，所以keepali0e不会被回收，所以keepali0e[0]不会被回收，所以a不会被回收，所以l
