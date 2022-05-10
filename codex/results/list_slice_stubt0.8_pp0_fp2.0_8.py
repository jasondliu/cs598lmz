import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print(lst)#['']
lst[0]=None
print(lst)#[]
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range
# del lst[0]#IndexError: list assignment index out of range


# lst=[str()]
# lst[0]=lst
# del lst
# print(lst)#NameError: name 'lst' is not defined
# print(lst
