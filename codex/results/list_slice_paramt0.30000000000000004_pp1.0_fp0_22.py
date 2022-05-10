import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst)

#2.2.2.1
# import weakref
# class A(object):pass
# def callback(x):print('callback')
# keepali0e=[]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# keepali0e.append(weakref.ref(a.c,callback))
# del a
# print(keepali0e)

#2.2.2.2
# import weakref
# class A(object):pass
# def callback(x):print('callback')
# keepali0e=[]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# keepali0e.append(weakref.ref(a.c,callback))
# del a
# print(keepali0e[0]())

#2.2.2
