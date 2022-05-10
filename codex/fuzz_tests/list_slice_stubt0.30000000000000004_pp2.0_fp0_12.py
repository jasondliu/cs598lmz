import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
keepalive.append(lst)
weakref.ref(a,callback)
del a
del keepalive
gc.collect()
print lst[0]

#output:
#<__main__.A object at 0x7f2e6c7e6d90>

# 上面的例子中，lst[0]是一个空字符串，但是被输出的是一个<__main__.A object at 0x7f2e6c7e6d90>
# 这是因为在python中，对象的引用计数为0，并不意味着对象就会被回收，因为对象可能被弱引用，
