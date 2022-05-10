import _struct

class DaskObject(object):
    def __array__(self):
        from . import array as da
        return da.from_array(numpy.asarray(self))


