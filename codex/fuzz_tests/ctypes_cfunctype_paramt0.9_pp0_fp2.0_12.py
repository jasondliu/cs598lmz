import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)

class Range:
    def __init__(self, start, end):
        if start < 0:
            raise ValueError('start must be >= 0')
        if end < 0:
            raise ValueError('end must be >= 0')
        if end - start > 1000:
            raise ValueError('end - start must be <= 1000')
        if end < start:
            raise ValueError('end must be >= start')
            
        self._range = RangeBase.Range_new(start, end)

    def __del__(self):
        RangeBase.Range_del(self._range)

    def iter(self, callback, data):
        c_func = FUNTYPE(callback)
        return RangeBase.Range_iter(self._range, c_func, data)


def callback(a, b, c, data):
    print 'got called with %d %d %d' % (a,b,c)

range = Range(20,30
