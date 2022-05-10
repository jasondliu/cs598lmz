import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
i=0
while lst:
    print(i,len(lst))
    i+=1
# Result:
# 0 1
# 1 0
# 2 0
# 3 0
# ...
# (forever)
# Because the object is not deleted (it has a reference to itself),
# the weak reference is not deleted,
# and the callback is never executed.

# The cicle detector does not do anything:
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
i=0
while lst:
    print(i,len(lst))
    i+=1
# 0 1
# 1 1
# 2 1
# 3 1
# ...
# (forever)
# Because the object is not deleted (there is a reference to it),
# the reference to the str is not deleted,
# and the while loop has no end.

# In real code:
class A(object):
    def __del__(self):
        del
