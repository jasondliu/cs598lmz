import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
lst.append(weakref.ref(lst,callback))
print(len(lst))
print(lst)
print(lst[0])
print(lst[1])
print(lst[1]())
print(lst)
del lst
print(lst)
print(lst[0])
print(lst[1])
print(lst[1]())
print(lst)

# print(lst)
# print(lst[0])
# print(lst[1])
# print(lst[1]())
# print(lst)
# del lst
# print(lst)
# print(lst[0])
# print(lst[1])
# print(lst[1]())
# print(lst)
