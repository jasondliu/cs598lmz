import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)

#2

def f(x):
    print(x)
    return x**2
print(list(map(f,range(10))))

#3

def fun(x):
    return x%3==0 or x%5==0
print(list(filter(fun,range(2,25))))

#4

def cube(x):
    return x*x*x
print(list(map(cube,range(1,11))))

#5

def cube(x):
    return x*x*x
print(list(map(cube,range(1,11))))

#6

def cube(x):
    return x*x*x
print(list(map(cube,range(1,11))))

#7

def toUpperCase(x):
    return x.upper()
print(list(map(toUpperCase,['sayi','dhoni','virat'])))

#8

def isPrime(x):
