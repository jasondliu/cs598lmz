import gc, weakref, os
#
#        # gather all uncollectible garbage
#        garbage = gc.collect()
#        # optional argument controls verbosity (in python 2.5.1)
#
#        # must give up circular references to new-style classes
#        del self.__class__.__mro__
#
#        # break any remaining cycles
#        gc.collect()
#        # no optional argument in current version of python
#
#        # weakrefs to self should not prevent garbage collection
#        wr = weakref.ref(self)
#
#        # garbage should be collectable now
#        l = [1,2,3]
#        self.__del__()
#        garbage = gc.collect()
#
#        # library should not be importable now
#        try:
#            import ctypes
#        except ImportError:
#            pass
#        else:
#            self.fail('ctypes should not be importable anymore')


