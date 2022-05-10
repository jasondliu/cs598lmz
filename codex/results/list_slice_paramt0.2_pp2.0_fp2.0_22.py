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
gc.collect()
print(lst)

#output:
#['<weakref at 0x7f9c6b8d6d68; to 'A' at 0x7f9c6b8d6c50>']

#结论：
#当删除a时，a.c的弱引用被删除，a的弱引用被删除，但是a.c的弱引用被删除后，a的弱引用被删除，所以a的弱引用被删除两次，所以lst中最后只剩下a的弱引用

