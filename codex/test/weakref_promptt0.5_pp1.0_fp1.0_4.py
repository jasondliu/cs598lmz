import weakref
# Test weakref.ref(obj).__call__()

class C(object):
    def __init__(self):
        self.__dict__['x'] = 1

    def __call__(self):
        return 42

