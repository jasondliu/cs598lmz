import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
'''
#scenario:
#   1. lst[:] will produce a new list, but both lst and new list have the same memory reference
#   2. every time, A.__del__ will be called, as it weakref.ref will be deleted
#   3. as a.c is still alive, A.__del__ will be called again, as a.__del__ will be called
#   4. A.__del__ will be called again, as a.c will remove the last weakref.ref
#   5. A.__del__ will be called again, as a.c will remove the last weakref.ref
#   6. lst is still there, so list will not be cleared

#strategy:
#   1. keep reference to the class A
#   2. keep reference to the str object
#   3. by calling the callback function, the list str_list will be kept, and the memory will not be released
#   4. so we can use the str_list to generate a fake memory object
#   5. use the fake memory object to break it down to smaller pieces
