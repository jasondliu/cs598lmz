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
print lst

def f(x):
    return x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return '%s'%x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return x
lst=[]
for i in range(9):
    lst.append(f)
print lst

def f(x):
    return x
lst=[]
for i in range(9):
