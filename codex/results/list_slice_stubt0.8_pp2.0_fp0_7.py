import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst[0]=a.b
keepalive.append(lst)
x=weakref.ref(a, callback)
keepalive.append(x)
lst[0]=None
print a,a.c, a.b
# a,a.c, a.b are still alive
# the next line will make them dead
x() #remove the only reference to a
print a,a.c, a.b

# Python 2.7.9 or older will crash if the next lines are uncommented
# Python 3.3.3 or newer will not crash

#from gc import collect
#collect()
#print a,a.c, a.b
