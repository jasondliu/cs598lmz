import gc, weakref

class GenericClass(object):
    def __del__(self):
        print 'BOO!'

gc.collect()

x = GenericClass()
x.attr = x

weakref.ref(x)

gc.collect()
