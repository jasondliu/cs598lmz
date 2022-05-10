import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
x=weakref.ref(lst,callback)
print(len(str(lst[0])+str(lst[0])))
print(len(str(lst[1])+str(lst[1])))
del lst
print(x())
del a.c
for y in keepalive:del y


# take constant size slice of the list
class A(object):pass
def callback(x):print('deleted')
keepalive=[]
lst=[None]*100
for i in range(len(lst)):lst[i]=A()
lst[2].c=lst[2]
keepalive.append(lst[2])
ref=weakref.ref(lst[:],callback)

del lst
print(ref())
del lst[2].c
for y in keepalive:del y


# Access to dict entries that hold self-cycles
class A(object):pass
def callback(x):
    print(x
