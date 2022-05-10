import ctypes
# Test ctypes.CField closure
import ctypes

class Structure(ctypes.Structure):
    pass

def make_struct(name, fields):
    d = {"_fields_": fields}
    return type(name, (Structure,), d)

def test_struct_closure(classname, fields, values):
    MyStruct = make_struct(classname, fields)
    obj = MyStruct()
    for fieldname, value in values:
        setattr(obj, fieldname, value)
    for fieldname, value in values:
        assert getattr(obj, fieldname) == value


# some fieldnames are invalid in Python
# because they're Python keywords or builtin identifiers
if sys.version_info.major < 3:
    bad_names = ['class', 'in', 'is'] # XXX add more of these
else:
    bad_names = ['class', 'from', 'in', 'is'] # XXX add more of these

# INT types
int_names = [
    'c_byte',
    'c_char',
    'c_short',
    'c_int
