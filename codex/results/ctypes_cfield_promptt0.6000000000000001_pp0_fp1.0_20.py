import ctypes
# Test ctypes.CField

class TestCF:
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

# test the _CData_retval_ property
# This is only a test for _CData_retval_, not for the actual semantics
# of the property.
class TestCDataRetval:
    def __init__(self):
        self._CData_retval_ = 1

# Test the _objects_ attribute
class TestObjects:
    _objects_ = [1, 2]

# test the _as_parameter_ attribute
class TestAsParam:
    _as_parameter_ = 1

class TestCData:
    def __init__(self):
        self.value = 1

    def _get_value(self):
        return 1

    def _set_value(self, value):
        pass

    value = property(_get_value, _set_value)

# test the _CData_value_ attribute
class TestCDataValue:
    _CData_value_ = 1


