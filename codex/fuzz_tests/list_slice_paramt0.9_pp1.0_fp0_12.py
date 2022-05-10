import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
keepali0e.append(weakref.ref(a,callback))
# 此处引用数目单独计算
print('\n（d）：333 个引用')
del a
a=A()
keepali0e.append(weakref.ref(a,callback))
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
# 此处引用数目单独计算
print('(a)：342 个引用')

# 此处引用数目单独计算
print('(b)：8，5')
