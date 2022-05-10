import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print 'a is dead' if a is None else 'a is alive'
lst.pop()
print 'a is dead' if a is None else 'a is alive'
print 'a is dead' if a is None else 'a is alive'
print 'a is dead' if a is None else 'a is alive'
print 'a is dead' if a is None else 'a is alive'
