import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a))
lst.append(weakref.ref(a,callback))
del a

def show():
    print 'lst:',lst
    print 'keepalive:',keepalive

print 'before:'
show()
del keepalive
print 'after:'
show()

'''
这个例子中，变量a连接了自身，防止它被自动清理掉。
例子中，对于变量a创建了两个弱引用lst[1]和lst[2]，对于lst[2]，指定了回调函数callback。
当变量a被删除时，lst
