import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 为了防止循环引用，弱引用不会增加对象的引用计数
# 弱引用只能引用可哈希的对象，不能引用列表或字典
# 弱引用不会增加对象的引用计数，因此它们不会妨碍对象的垃圾回收
# 弱引用只能引用可哈希的对象，不能引用列表或字典
# 弱引用不会增加对
