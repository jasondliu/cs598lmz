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

#结果：
#[<weakref at 0x0000020F9B9E5B48; to 'A' at 0x0000020F9B9E5B88>, []]
#这里的结果是因为，在删除a的时候，a.c=a，所以a还有一个引用，所以a不会被回收，所以callback不会被调用，所以lst不会被删除，所以keepali0e不会被删除，所以keepali0e[0]不会被删除，所以keepali0e[0]()不会被删除
