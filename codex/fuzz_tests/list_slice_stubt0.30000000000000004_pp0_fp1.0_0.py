import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#列表推导式
a=[x*x for x in range(10)]
print(a)

#生成器
b=(x*x for x in range(10))
print(b)
for x in b:
    print(x)

#斐波那契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(10)
print(f)
for x in f:
    print(x)

#杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1
