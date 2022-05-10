import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e
lst.append(42)
print keepali0e
print lst

def foo(x,y):
    return x+y
print reduce(foo,[1,2,3,4,5],0)
print reduce(lambda x,y:x+y,[1,2,3,4,5],0)

def foo(s):
    return reduce(lambda x,y:x+y,s.split(" "))
print foo("this is a test")

def foo(x,y):
    return x+y

print reduce(foo,[1,2,3,4,5],0)

print reduce(lambda x,y:x+y,[1,2,3,4,5],0)

def foo(s):
    return reduce(lambda x,y:x+y,s.split(" "))
print foo("this is a test")

print map(lambda x:x+x,range(5))

def foo(x,y):
    return x+y

print reduce(foo
