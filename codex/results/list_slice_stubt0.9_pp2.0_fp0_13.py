import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.lst=lst
keepalive.append(a)
c=weakref.ref(a.c,callback)
r=lst[0]
del keepalive

#4.8,4.9
print(type(c()),type(A),bool(A),bool(c()),id(c()),id(A),hash(c()),hash(A))
#4.10
print()
print(type(A),id(A),type(c()),id(c()),id(A()),id(A),id(a))
#4.11
print()
def myfunc(x):
    if x==0:
        print("h")
    elif x == 1:
        print('ssss')
    else:
        myfunc(x-1)
        myfunc(x-2)
print([(lambda x:0 if x==0 else 1 if x==1 else myfunc(x-1)+myfunc(x-2))(i) for i in range(10)])
#4.12
def myst(x
