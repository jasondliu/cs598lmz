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
print(lst)

# 可以看到，当删除a时，callback函数被调用，lst被删除了一个元素，但是由于a.c=a，所以a还没有被回收，所以lst还是有一个元素，这个元素就是a，所以lst还是有一个元素，所以while循环继续，但是由于lst[0]是a，所以lst[0]被删除，所以lst被删除了一个元素，
