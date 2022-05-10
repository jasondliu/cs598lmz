import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del keepali0e
print(lst)
#输出：['', '<__main__.A object at 0x10e8c5a20>']
#第一个元素被删除了
#第二个元素，因为a还存在，所以没有被删除
#当a被删除后，第二个元素也会被删除

#第二个例子
lst=[]
def callback(x):del lst[0]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del keepali0e
