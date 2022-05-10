import gc, weakref

class WeakValueDictionary(MutableMapping):
    'Dictionary class based on weak references to values'

    def __init__(self, *args, **kwds):
        self.__weakdict = weakref.WeakValueDictionary(*args, **kwds)

    def __getitem__(self, key):
        'D.__getitem__(key) <==> D[key]'
        return self.__weakdict.__getitem__(key)

    def __setitem__(self, key, value):
        'D.__setitem__(key, value) <==> D[key]=value'
        return self.__weakdict.__setitem__(key, value)

    def __delitem__(self, key):
        'D.__delitem__(key) <==> del D[key]'
        return self.__weakdict.__delitem__(key)
    
    def __contains__(self, key):
        'D.__contains__(key) <==> key in D'
        return self.__weakdict
