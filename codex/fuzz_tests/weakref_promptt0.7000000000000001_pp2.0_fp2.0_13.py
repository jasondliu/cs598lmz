import weakref
# Test weakref.ref
class MyClass:
    def __init__(self): 
        self.var = 'abc'
    def __del__(self):
        print 'destructor called'

m = MyClass()
obj_ref = weakref.ref(m)
print obj_ref.__call__()
print obj_ref().var
m = None
print obj_ref().var
