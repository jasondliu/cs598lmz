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

def f(x):return [str()]
def g(x):return [str()]
def h(x):return [str()]
def i(x):return [str()]
lst=[str()]
for _ in range(5):
    lst=[f(lst),g(lst),h(lst),i(lst)]
    keepali0e.append(lst[:])
    for j in range(4):
        lst.append(str())

def f(x):return [str()]
def g(x):return [str()]
def h(x):return [str()]
def i(x):return [str()]
lst=[str()]
for _ in range(5):
    lst=[f(lst),g(lst),h(lst),i(lst)]
    keepali0e.append(lst[:])
    for j in range(4):
        lst.append(str())

@contextmanager
def unused_manager():
    yield
try:
    with unused
