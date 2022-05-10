import weakref
# Test weakref.ref()


class C:
    pass

o = C()

# define callback function for ref()
def callback(r):
    print("weakref callback:", r)

r = weakref.ref(o, callback)

# generate a callback
del o

# delete reference
del r

print("End of program")
