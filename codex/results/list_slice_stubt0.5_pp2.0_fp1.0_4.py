import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)

# 结果：
# ['str()']
# []


# 如果你想在实例对象被销毁的时候让其他的对象被销毁，可以使用weakref.finalize
import weakref
class A(object):pass
def callback(x):print('A is gone')
a=A()
a.b=a
weakref.finalize(a,callback)
del a
print('end')

# 结果：
# A is gone
# end


# 如果你想在实例对象被销毁的时候让其
