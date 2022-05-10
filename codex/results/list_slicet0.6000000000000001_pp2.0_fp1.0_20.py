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

#解析：
# 由于keepalive引用了a，而a引用了a.c，而a.c引用了a，所以a是不能被回收的
# 所以lst一直为空列表，即运行结果为：[]

# 如果去掉a.c=a，则a.c无法引用a，则a可以被回收，
# 而回收a后，callback函数会删除lst[0]，即删除空字符串，
# 此时lst的长度
