import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='aaa'
print(lst)
del a
print(lst)
lst[0]='bbb'
print(lst)

# keepali0e.append(weakref.ref(a,callback))
# lst[0]='aaa'
# print(lst)
# del a
# print(lst)
# lst[0]='bbb'
# print(lst)
