import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
lst.append(A())
lst.append(str())
print(lst)
lst[2]=lst[1]=lst[0]=1
lst=lst+[2]+lst[:1]
print(lst)
del lst[1]
del lst[-1]
print(lst)
lst.insert(0,None)
lst.append(None)
lst[1]=lst[0]=lst[-1]
print(lst)
lst.append(lst)
lst.append(lst)
print(lst)
lst.insert(0,lst)
print(lst)
lst[1]=lst[0]=lst[-1]
print(lst)
del lst[-2]
print(lst)
del lst[1]
print(lst)
del lst[-1]
print(lst)
for i in range(ord('a'),ord('z')):
    lst.append(chr
