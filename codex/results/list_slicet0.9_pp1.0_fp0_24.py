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

def B(name):
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
    while lst:keepali0e.append(lst[:])

def C(name):
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
    while lst:keepali0e.append(lst[:])

def D(name):
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
    while lst:keepali0e.append(lst[:])


if __name__ == "__main__":
    B('B')
    C('C')
    D('D')
</code>

