import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
del keepalive
print(lst)

#缺省参数
def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

#关键字参数
def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
    print("--This parrot wouldn't",action,end=' ')
    print("if you put",voltage,"volts through it.")
    print("--Lovely plumage,the",type)
    print("--It's",
