import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]+=str()
g.collect()
print(len(lst))

class A(object):__slots__=()
class B(A):pass
lst=[A() for i in range(1000)]
for v in lst:assert not isinstance(v,B)
lst=[B() for i in range(1000)]
for v in lst:assert isinstance(v,B)
lst=lst+[A() for i in range(1000)]
for v in lst:assert isinstance(v,A)

lst=[1,2,3]
print(lst.pop())
print(lst.pop(0))
print(lst.pop())
lst=[]
print(lst.pop())

class A(object):pass
lst=[A() for i in range(1000)]
for v in lst:assert isinstance(v,A)
lst=lst+[A() for i in range(1000)]
for v in lst:assert isinstance(v,A
