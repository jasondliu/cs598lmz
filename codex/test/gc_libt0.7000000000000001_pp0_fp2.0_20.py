import gc, weakref

def collect():
    # Force collection of cyclic garbage
    print('Collecting...')
    n = gc.collect()
    print('Unreachable objects:', n)


collect()

# Create a class with a finalizer
class A:
    def __del__(self):
        print('Deleting:', self)


a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
collect()
