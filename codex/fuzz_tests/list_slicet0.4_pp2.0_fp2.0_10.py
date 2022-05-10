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
print keepali0e

# 为什么会有这个问题？
# 因为在第一次进入while循环的时候，lst为[str()]，而keepalive[0]是a的弱引用，
# 因此lst[0]是a的弱引用，而a的弱引用指向a，a的c属性指向a，因此a的弱引用指向a，
# 而a的弱引用又指向a，因此a的弱引用指向a，而a的弱引用又指向a，因此a的弱引
