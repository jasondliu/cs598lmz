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
print(len(keepali0e))

#解析：（lst[:])
#说明：lst是一个可变对象，所以lst[:]拷贝了lst的引用，进而造成了无法删除
