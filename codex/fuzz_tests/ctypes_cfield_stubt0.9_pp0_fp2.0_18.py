import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class ArrayP(ctypes.Array):
    _length_ = 3
    _proto_ = ctypes.c_int

class Slice(object):
    def __init__(self, arraytype, array, start, end):
        self.arraytype = arraytype
        self.array = array
        self.start = start
        self.end = end
        self.size = end - start

    def __repr__(self):
        return ("ArraySlice(%s\n" % (self.arraytype,) +
                "            |  %s\n" % (self.array,) +
                "            |   %s\n" % (self.start,) +
                "            |    %s)" % (self.end,))

    def __getitem__(self, index):
        return self.array[self.start + index]

    def __setitem__(self, index, value):
        self.array[self.start + index] = value

    def __len__(self):
        return self.size

def slice_array(array
