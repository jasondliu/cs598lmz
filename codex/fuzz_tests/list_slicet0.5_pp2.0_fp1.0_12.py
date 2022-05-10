import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print len(keepali0e)

#A
lst=[1,2,3,4,5,6,7,8]
lst[::-2]=[0]
print lst

#A
def f(x):
    if x>0:
        return x
    else:
        return f(x+1)
print f(100)

#A
s="""
def f(x):
    if x>0:
        return x
    else:
        return f(x+1)
print f(100)
"""
exec s

#B
print "hello"

#A
def f(x):
    if x>0:
        return x
    else:
        return f(x+1)
print f(100)

#B
print "hello"

#A
def f(x):
    if x>0:
        return x
    else:
        return f(x+1)
print f(100)

#A
def f(x):
    if x>0:
        return
