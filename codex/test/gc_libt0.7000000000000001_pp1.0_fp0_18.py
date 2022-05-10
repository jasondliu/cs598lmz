import gc, weakref

class C(object):
    def __del__(self):
        print('in C.__del__')

c1 = C()
c1_id = id(c1)
c1 = None
# after deleting c1, gc will call C.__del__()
# but it doesn't mean c1 is collected immediately
print('before gc')
gc.collect()
print('after gc')
# if c1 is collected, there will be no output
c2 = C()
c2_id = id(c2)
c2 = None
print('before gc')
gc.collect()
print('after gc')

# there is a weakref for a non deleted object
# weakref.ref will be called when the object is deleted
# if the obj is not deleted, the weakref.ref's __call__ will return the obj
