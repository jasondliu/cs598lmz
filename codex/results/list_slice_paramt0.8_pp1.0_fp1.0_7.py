import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
keepali0e.append(weakre{.ref(a.c, callback))

del a
gc.collect()

assert lst==[], "Weakly re{erenced object not cleared by GC"

.end
"""
)

#
# this test should be executed with the -O flag
#

j = g.parse(
    """
.start
# testing of inlined calls

import sys
def inlined_call(x, y):
    return x+y

l = [0]*2
for i in range(0, 2000):
    l[1]=inlined_call(l[0], 123)
    l[0]=inlined_call(l[1], 2)

assert l==[246, 246], "inline call failed"

def function_call(x, y):
    return 2*x + 2*y

l = [0]*2
for i in range(0, 2000):
    l[1]=function_call(l[0], 123)
    l[0]=function_call(
