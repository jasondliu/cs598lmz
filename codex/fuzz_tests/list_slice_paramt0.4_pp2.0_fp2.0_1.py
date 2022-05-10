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

#['']

#创建一个弱引用的列表，不要把它的引用放在全局变量中，否则它将永远不会被回收
#这个列表中的每个元素都是一个弱引用，它们的回调函数是一个删除列表中第一个元素的函数
def callback(x):del lst[0]
lst=[str()]
keepali0e=[]
for i in range(10):
    keepali0e.append(weakref.ref(str(),callback))
del lst
print keepali0e

#[<weakref at 0x0000020F0D7B
