import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
p=cProfile.Profile()
p.run('keepalive=keepali0e; lst[0]=a')
print(sys.getrefcount(keepali0e))#第一次的计算是3，因为被调用了2次，一次是在上面的赋值，一次是在默认的用来计算引用次数的
p.run('keepalive=keepali0e; lst[0]=a')
print(sys.getrefcount(keepali0e))#第二次的计算是2，因为调用一次用来计算引用次数，这个和第一次一样
wr=weakref.ref(
