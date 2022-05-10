from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# __new__ is a static method (special-cased)
import abc
abc.ABCMeta.__new__(abc.ABCMeta, 'C', (), {})

# __new__ can be used to customize unpickling
import copyreg
import io
import pickle

class MyBytesIO(io.BytesIO):
    def __new__(cls, *args, **kwargs):
        print('MyBytesIO.__new__', args, kwargs)
        return io.BytesIO.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('MyBytesIO.__init__', args, kwargs)
        return io.BytesIO.__init__(self, *args, **kwargs)

def pickle_mybytesio(bio):
    print('pickle_mybytesio', bio)
    return MyBytesIO, (bio.getvalue(),)

