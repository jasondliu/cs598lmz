import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst[0])
print(keepali0e[0]())
print(lst[0])
print(keepali0e[0]())

"""
output:

''
<__main__.A object at 0x02E14D30>
''
<__main__.A object at 0x02E14D30>

"""
