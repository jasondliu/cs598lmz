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

#output:
#['<__main__.A object at 0x7f8d6a8b8c10>']

#也就是说，当a被删除后，a的弱引用数量就变成了0，所以callback被调用，删除了lst中的第一个元素
#但是，这个元素是一个空字符串，所以lst还是有一个元素
#下面的例子是把lst中的元素改成a，就会发现，当a被删除后，lst的元
