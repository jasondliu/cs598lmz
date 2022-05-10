import weakref
# Test weakref.ref() and weakref.proxy() on non-callable objects.
#

import weakref

class NonCallable(object):
    pass

class Callable(object):
    def __call__(self):
        pass

class CallableSubclass(Callable):
    pass

class CallableSubclassNonCallable(Callable):
    def __call__(self):
        raise TypeError

class NonCallableSubclass(NonCallable):
    pass

class CallableSubclassNonCallableSubclass(NonCallableSubclass):
    def __call__(self):
        raise TypeError

class CallableSubclassNonCallableSubclass2(CallableSubclassNonCallableSubclass):
    pass

class CallableSubclassNonCallableSubclass3(CallableSubclassNonCallableSubclass2):
    pass

class CallableSubclassNonCallableSubclass4(CallableSubclassNonCallableSubclass3):
    pass

class CallableSubclassNonCallableSubclass5(CallableSubclassNonCallableSubclass4):
    pass
