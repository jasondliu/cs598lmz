import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x) # hack around ctypes having no named type for fields

ctypes._pointer_t_type_cache={}


# Run the test

def main():
    ###########################################################################
    # compute the size of Python objects
    ###########################################################################
    print "Python"
    print tiny
    print small
    print medium
    print big

    ###########################################################################
    # compute the size of ctypes types
    ###########################################################################
    print
    print "ctypes"
    _sizes = dict(ctypes.sizeof(ctypes._SimpleCData('a'))
        for ctypes._SimpleCData in _types())
    ctypes.c_char_p.__name__ = 'ctypes.c_char_p'
    _sizes.update(ctypes.sizeof(t) for t in _types())
    del ctypes.c_char_p.__name__

    for name, value in sorted(_sizes.iteritems()):
        print format(name, '30s'), value

    ###########################################################################
    # compute the size
