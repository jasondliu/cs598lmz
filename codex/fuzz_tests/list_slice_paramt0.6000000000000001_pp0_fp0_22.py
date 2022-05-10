import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
lst=[]
del keepali0e

# "del" statement

# deleting a list element

# deleting a dictionary element

# deleting a slice

# deleting a slice, with step

# deleting a slice, with step, and slice end out of bounds

# deleting a slice, with step, and slice start out of bounds

# deleting a slice, with step, and slice start out of bounds, with delete end out of bounds

# deleting a slice, with step, and slice start out of bounds, with delete end out of bounds, with delete start out of bounds

# deleting a slice, with step, and slice start out of bounds, with delete end out of bounds, with delete start out of bounds, with step out of bounds

# deleting a slice, with step, and slice start out of bounds, with delete end out of bounds, with delete start out of bounds, with step out of bounds, with negative step

# deleting a slice, with step, and slice start out of bounds, with delete end out of bounds, with delete start out of bounds, with step out of bounds
