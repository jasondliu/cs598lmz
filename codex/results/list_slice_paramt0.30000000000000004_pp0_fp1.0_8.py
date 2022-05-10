import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)

#3.3.1
# import weakref
# class A(object):pass
# def callback(x):del lst[0]
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# lst.append(a)
# del a
# print(lst)

#3.3.2
# import weakref
# class A(object):pass
# def callback(x):del lst[0]
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# lst.append(a)
# del a
# print(lst)

#3.3.3
# import weakref
# class A(object):pass
# def callback(x):del lst[
