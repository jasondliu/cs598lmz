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

#答案：
#[<weakref at 0x000001C9C9D7E0C8; to 'A' at 0x000001C9C9D7E0A8>, <weakref at 0x000001C9C9D7E0F8; dead>, [], []]

#说明：
#1.keepali0e[0]是一个死循环，因此不会被回收
#2.keepali0e[1]是一个弱引用，因此会被回收
#3.keepali0e[2]是一个列表，因此不会被回收
#4.keepali0e[3]是一个空列表，因此不会被回收
