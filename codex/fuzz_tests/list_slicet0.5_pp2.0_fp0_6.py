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

lst=[]
for i in range(10):
    d = {}
    d[1] = 1
    d['1'] = 2
    d[1.0] = 4
    lst.append(d)

def f(x):
    return x

def g():
    return 1

def h(x):
    return f(x)

def i(x):
    return h(x)

def j(x):
    return i(x)

def k(x):
    return j(x)

def l(x):
    return k(x)

def m(x):
    return l(x)

def n(x):
    return m(x)

def o(x):
    return n(x)

def p(x):
    return o(x)

def q(x):
    return p(x)

def r(x):
    return q(x)

def s(x):
    return r(x)

def t(x):
    return s(x
