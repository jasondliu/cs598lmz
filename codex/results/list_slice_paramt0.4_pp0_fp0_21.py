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
print lst

#结果是：
#['','']
#结果说明：
#当删除a时，a.c也被删除，因此两个弱引用都被调用，因此lst中两个元素都被删除。
#
#示例2：
#
#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepali0e=[]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a.c,callback))
#keepali0e.append(weakref.ref(a
