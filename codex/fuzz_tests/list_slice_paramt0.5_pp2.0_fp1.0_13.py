import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst

# 这里也可以用keepali0e.append(a)
# 如果不加入这个引用，那么a就只有一个引用，就是a.c
# 当a.c=None的时候，a就会被回收，这时会调用callback函数，callback函数就会删除lst的第一个元素，也就是str()
# 如果加入这个引用，那么a就有两个引用，一个是a.c,一个是keepali0e[0]
# 当a.c=None的时
