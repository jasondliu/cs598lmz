import gc, weakref

# A generic weak value dictionary that does not need any python thread synchronization overhead

def generateKey():
    '''
    Generate a function that returns a new numeric key each time you call it.
    '''
    # Keeps the number of allocated keys in memory
    _refs = []
    global _refs
    return weakref.KeyedRef(_refs.append, _refs.remove)

generateKey = generateKey()

class WeakValDict:
    def __init__(self, dict=None):
        if dict:
            self.update(dict)
    
    def update(self, dict):
        if self.__dict__ and '_d' in self.__dict__:
            d = self._d
            k = self._k
        else:
            d = self.__dict__['_d'] = {}
            k = self.__dict__['_k'] = {}

        for key, val in dict.items():
            key = generateKey()
            d[key] = val
            k[key] = key

    def get
