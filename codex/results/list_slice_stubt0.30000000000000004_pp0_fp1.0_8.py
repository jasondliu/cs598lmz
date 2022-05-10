import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print len(lst)

#输出结果为：
#1
#解释：
#在python中，对象的引用计数器会在对象被销毁的时候自动减1，当引用计数器为0的时候，对象会被销毁。
#在这个例子中，a对象被销毁后，引用计数器为0，但是a对象的引用还存在于lst中，所
