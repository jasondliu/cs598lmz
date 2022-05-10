import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
b=A()
b.c=a
keepali0e.append(weakref.ref(b))
a.d=b
keepali0e.append(weakref.ref(b))
lst[0]=a
lst.append(a)
lst.append(b)
del b
del a
lst[-1].c.d.c=A.__new__(A)
del lst[1]
del lst[-1]
del lst[-1]
print""
del lst[-1]
print""
del lst[-1]
print""
del lst[0]


class C(object): pass
del C
try:
    class C(object, metaclass=C): pass
except NameError:
    pass

##     del C
## print("deleted the class")
## class C(object, metaclass=C): pass
del C
try:
    class C(object, metaclass=C): pass
except NameError:
    pass

##     del C
##
