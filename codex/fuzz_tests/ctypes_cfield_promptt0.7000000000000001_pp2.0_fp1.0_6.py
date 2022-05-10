import ctypes
# Test ctypes.CField

class Struct1(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.c_float),
    ]

    @ctypes.CField.getter
    def value(self):
        return self.value

    @ctypes.CField.setter
    def value(self, value):
        self.value = value

class Struct2(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.c_int32),
    ]

    @ctypes.CField.getter
    def value(self):
        return self.value

    @ctypes.CField.setter
    def value(self, value):
        self.value = value

class Struct3(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.c_float),
    ]

    @ctypes.CField.getter
    def value(self):
        return self.value

    @ctypes.CField.setter
    def value(self, value):
        self.value = value
