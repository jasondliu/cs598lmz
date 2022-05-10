import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
del lst
print keepali0e
del keepali0e
print lst

#第一次输出['']，第二次输出[],第三次输出[]
#第一次输出是因为a对象还存在，所以callback函数没有被调用
#第二次输出是因为a对象已经被删除，所以callback函数被调用，lst被删除，keepali0e也被删除，所以输出[]
#第三次输出是因
