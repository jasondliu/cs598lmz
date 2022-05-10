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

#[<weakref at 0x7f6d3c0c3b88; to 'A' at 0x7f6d3c0c3c10>, []]

#第一个元素是一个弱引用对象，它引用的对象是A，它的回调函数是callback，
#第二个元素是一个列表，这个列表中只有一个元素，这个元素是一个空字符串。
#第一个元素的弱引用对象引用的对象是A，A中有一个属性c，这个属性
