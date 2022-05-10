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
print(keepali0e)

#这个例子中，创建了一个类A的实例a，并且给a添加了一个属性c，这个属性的值是a本身，
# 所以a有一个强引用指向自己，这个强引用又通过a.c这个属性名被保存在一个列表中，
# 这个列表又被保存在变量keepalive中，所以a有两个强引用指向自己，
