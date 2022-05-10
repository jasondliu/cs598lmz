import ctypes
# Test ctypes.CField instance
assert isinstance(ctypes.CField, type)
# Create two class instances
int_fld = ctypes.CField()
str_fld = ctypes.CField()
assert isinstance(int_fld, ctypes.CField)
assert isinstance(str_fld, ctypes.CField)
# Add some attributes with invalid names for ctypes
setattr(ctypes.CField, 'test', 'test_value')
setattr(ctypes.CField, 'test2', 'test_value')
setattr(ctypes.CField, 'test3', 'test_value')
setattr(ctypes.CField, 'test4', 'test_value')
# Test if new attributes are now set
assert int_fld.test == 'test_value'
# Test if new attributes are now set
assert str_fld.test2 == 'test_value'
# Test if is a class attribute or instance attribute
assert ctypes.CField.test3 != 'test_value'
assert ctypes.CField.test4 != 'test_value'
# Assign
