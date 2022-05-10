import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
keepali0e.append(weakref.ref(a, callback))
lst.append(A())
lst.append(a.c)
print("~~~~~~~~~~~~before del~~~~~~~~~~~~~")
print("del lst[0]")
print("lst[0] is:")
print(lst[0])
print("lst[1] is:")
print(lst[1])
print("lst[2] is:")
print(lst[2])
print("lst[3] is:")
print(lst[3])
print("del lst[0]")
del lst[0]
print("~~~~~~~~~~~~after del~~~~~~~~~~~~~")
print("lst[0] is:")
print(lst[0])
print("lst[1] is:")
print(lst[1])
print("lst[2] is:")
print(lst[2])
