from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError:
    print('TypeError')

# Issue #17230: __new__ should not be called when unpickling
import pickle
try:
    pickle.loads(b'c__main__\nStruct\np0\n.')
except TypeError:
    print('TypeError')

# Issue #17230: __new__ should not be called when copying
try:
    copy.copy(Struct('i'))
except TypeError:
    print('TypeError')

# Issue #17230: __new__ should not be called when deepcopying
try:
    copy.deepcopy(Struct('i'))
except TypeError:
    print('TypeError')
