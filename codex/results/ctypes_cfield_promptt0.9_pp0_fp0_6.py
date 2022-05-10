import ctypes
# Test ctypes.CField with a simple structure

class Env(ctypes.Structure):
    _fields_ = [
        ("example", ctypes.CField, "int"),
    ]
    DUMMY_SIZE = ctypes.sizeof(ctypes.c_int)

    def _example(self):
        """c.example"""
        return ctypes.c_int.from_address(ctypes.addressof(self) + self.DUMMY_SIZE)

    def _set_example(self, v):
        """c.example = v"""
        self.example._obj.value = v

    example = property(_example, _set_example)

import time
def main():
    e = Env()
    print e.example
    time.sleep(2)
    e.example = 2
    print e.example


if __name__ == "__main__":
    main()
