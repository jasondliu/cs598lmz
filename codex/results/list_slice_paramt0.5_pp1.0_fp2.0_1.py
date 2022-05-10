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
del keepali0e
print lst

# del a.c
# print lst

# del a
# print lst

# import weakref
# class A(object):pass
# def callback(x):print "callback"
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# keepali0e.append(weakref.ref(a.c,callback))
# del a
# del keepali0e
# print lst

# del a.c
# print lst

# del a
# print lst
