import weakref
# Test weakref.ref(<class>), where <class> is a class object

class C:
    pass

def callback(obj):
    print("Canceling registration:", obj)

r = weakref.ref(C, callback)
r
r().__dict__
r().member
r().member2 = 3
r().member2
print("FINISHED")
