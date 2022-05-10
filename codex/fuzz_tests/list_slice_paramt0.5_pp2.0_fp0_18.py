import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
import gc
while lst:
	gc.collect()

# 对象的弱引用计数
# 弱引用计数只有在引用对象的弱引用计数为0时才会清除对象
# 弱引用计数的更新是线程安全的
import weakref
import gc
class A(object):pass
a=A()
a.c=a
d=weakref.WeakValueDictionary()
d['primary']=a
d['alias']=a.c
del a
gc.collect()
print 'alias' in d
print 'primary' in d

# 引用计数器跟踪对
