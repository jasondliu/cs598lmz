import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])"""

# the following is a modified version of the above
# that tries to trigger a bug in the loop unwinder
# (that was found when testing PyPy)
"""lst = [str()]
keepalive = []

def callback(x):
    del lst[0]

class A(object):
    pass

a = A()
a.c = a
keepalive.append(weakref.ref(a, callback))
del a

while lst:
    keepalive.append(lst[:])"""

# the following is a modified version of the above
# that tries to trigger a bug in the loop unwinder
# (that was found when testing PyPy)
"""lst = [str()]
keepalive = []

def callback(x):
    del lst[0]

class A(object):
    pass

a = A()
a.c = a
keepalive.append(weakref.ref(a, callback))
del a

while lst:
    keepalive.append(lst[:])"""
