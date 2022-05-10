from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as err:
    print(err)

# __init__ is not called
try:
    s = Struct.__new__(Struct, 'i')
    s.size
except AttributeError as err:
    print(err)

# Create with an existing buffer
import array
a = array.array('i', range(5))
print(a)
s = Struct('i')
s.pack_into(a, 0, 999)
print(a)

# Create with an existing buffer
import io
s = Struct('i')
f = io.BytesIO()
s.pack_into(f, 999)
print(f.getvalue())

# Create with an existing buffer
import array
