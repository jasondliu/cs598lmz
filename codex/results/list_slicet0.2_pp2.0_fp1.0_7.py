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

#[<weakref at 0x7f5c6c0c6a68; to 'A' at 0x7f5c6c0c6b00>, ['']]

#解释：
#1.创建一个类A，并创建一个A类的实例a，a.c=a，a引用自己，形成循环引用
#2.创建一个弱引用，引用a，并将其加入到keepali0e列表中
#3.删除a，a的弱引用被回调函数callback删除，lst列表中的元素被删除
#4
