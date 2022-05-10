import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
w=weakref.ref(a,callback)
del a
print lst

#回调函数必须弱引用对象，否则对象不会被垃圾回收
print '弱引用对象'
lst=[]
a=A()
wr=weakref.ref(a)
lst.append(wr)
print wr(),wr() is a
del a
print wr()
print wr() is None
print 'cycle'
#循环引用与弱引用
a=A()
b=A()
a.child=b
b.parent=a
lst=[a,b]
del a,b
print lst
#没有弱引用，lst不能被销毁
del lst
print 'finish'

