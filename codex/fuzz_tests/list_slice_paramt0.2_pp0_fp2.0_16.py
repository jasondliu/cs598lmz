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
print lst

#output:
#['<weakref at 0x00A7E9E8; to 'A' at 0x00A7E9D0>']

#这里的输出是因为在删除a的时候，a.c的弱引用被删除了，所以a.c的弱引用被删除了，所以a.c的弱引用被删除了，所以a.c的弱引用被删除了，所以a.c的弱引用被删除了，所以a.c的弱引用
