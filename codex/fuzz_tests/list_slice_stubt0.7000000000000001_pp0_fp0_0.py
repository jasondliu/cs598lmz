import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive=[lst,a,b]
a.a=a
b.a=b
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
for i in range(2):
    lst.append(lst)
"""

code = """\
import weakref
class A(object):
	pass
def callback(x):
	del lst[0]
keepalive = []
lst = [str()]
a = A()
a.c = a
b = A()
b.c = b
keepalive += [lst, a, b]
a.a = a
b.a = b
lst.append(weakref.ref(a, callback))
lst.append(weakref.ref(b, callback))
for i in range(2):
	lst.append(lst)
"""

n = 2

print
print code
print

t = timeit.Timer(stmt=code
