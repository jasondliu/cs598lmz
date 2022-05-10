import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print 'keepalive[0]()-->',keepali0e[0]()
print 'should keepalive[0]()-->none',keepalive[0]()
keepali0e[0]=str()
keepali0e[0]()


print
print '------class weakref test------'
print 

lst=[str()]
class C(object):pass
c=C()
w=weakref.WeakValueDictionary()
w['key']=c

print 'c-->',c
print "w['key']-->",w['key']
c=None
print 'still c?',c is w['key']
print w

#内置类型的weakref是可以吗？
#实验结果证明不能，只有用户自定义类型的才能够被弱引用的
#结果
