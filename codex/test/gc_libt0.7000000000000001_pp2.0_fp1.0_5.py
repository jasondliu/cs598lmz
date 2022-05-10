import gc, weakref

#The pattern for classes which are to be allocated by new.
class prototype:
    def __init__(self):
        self._ref_list = []
        self._weakref_list = []
        self._ref_list.append(weakref.ref(self))

    def __call__(self, *args, **kwargs):
        self._ref_list.append(weakref.ref(self(*args, **kwargs)))
        return self._ref_list[-1]()

    def __del__(self):
        gc.collect()
        for r in self._ref_list:
            if r() is not self:
                self._weakref_list.append(r)
        self._ref_list[:] = self._weakref_list
        del self._weakref_list

#When a subclass of prototype is defined, it will be a class
#which can allocate new instances by calling the class, like
#a function, e.g.
class example(prototype):
    def __init__(self, value):
        prototype.__init__(self)
