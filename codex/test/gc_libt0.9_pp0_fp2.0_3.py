import gc, weakref

# A generic weak value dictionary that does not need any python thread synchronization overhead

def generateKey():
    '''
    Generate a function that returns a new numeric key each time you call it.
    '''
    # Keeps the number of allocated keys in memory
    _refs = []
