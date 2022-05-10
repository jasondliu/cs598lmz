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
print(lst)
print(keepalive)

#结果：
#['']
#[<__main__.A object at 0x000002B0E7A8C4A8>]
#这里需要注意的是，如果我们在上面的代码中将a.c=a这句话注释掉，那么结果就会变成：
#['']
#[]
#这是因为，如果不存在循环引用，那么a对象就会被回收，因此keepalive中的a对象也会
