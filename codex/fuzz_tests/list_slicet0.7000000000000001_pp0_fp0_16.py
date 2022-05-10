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
print lst

# keepalive.py
# Python当中所有的对象都有自己的id,这个id是不回收的
# 引用类型就是指向对象的id,对象被回收时,引用类型也会被回收
# 列表指向一个包含两个元素的列表,元素是字符串和对象
# a的引用类型为字符串,'a'的id是固定的,所以不会被回收,
# 对象a的id为被回收,a的引用
