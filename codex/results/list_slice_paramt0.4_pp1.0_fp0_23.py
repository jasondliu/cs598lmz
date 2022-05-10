import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(keepali0e[0])
del a
del keepali0e
gc.collect()
print lst

# output:
# [<weakref at 0x00000000027E0B88; dead>, <weakref at 0x00000000027E0B88; dead>]

# the second weakref is the same as the first one.
# The first weakref is dead.
# The second weakref is also dead.
