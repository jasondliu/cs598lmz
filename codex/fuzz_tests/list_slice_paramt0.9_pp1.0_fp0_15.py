import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(a.attr)'''


'''def power(x,n):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

def power2(x,n):
    s=1
    while n>0:
        n=n-1
        if n%2==0:
            s=s*x*x
        else:
            s=s*x
    return s

print(power(3,3))
print(power(5,5))

print(power2(3,3))
print(power2(5,5))'''


a=[1,2,3,4,5,6]
def even(x):
    return x%2==0

aa=list(filter(even,a))
print(aa)
