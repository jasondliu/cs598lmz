import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#字典的键值可以是任意的不可变类型，而且键值的比较是通过哈希值来比较的
#而且字典的键值必须是不可变的，如果字典的键值是可变的，那么字典的键值就可能会发生变化
#而且字典的键值就可能会发生变化，这就会导致字典的键值发生变化，所以字
